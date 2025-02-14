from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import requests
import json

app = Flask(__name__)
JWT_SECRET_KEY = "ID3z2UXcWBQ8q__U4q7UNUcHdkqIQoqTwoPDcyTdACk"
app.secret_key = JWT_SECRET_KEY

API_BASE_URL = "https://todo-list-project-z4fl.onrender.com/"

@app.route("/")
def index():
    """Renders the Home Page"""
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    """Redirects authenticated users to their task list"""
    if "token" not in session:
        return redirect(url_for("login"))

    headers = {"Authorization": f"Bearer {session['token']}"}
    response = requests.get(f"{API_BASE_URL}/tasks", headers=headers)
    tasks = response.json() if response.status_code == 200 else []

    return render_template("tasks.html", tasks=tasks)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Handles user registration (JSON Input)"""
    if request.method == "POST":
        try:
            data = request.get_json()
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or not email or not password:
                return jsonify({"message": "All fields are required"}), 400

            username = username.replace(" ", "_")  # Convert spaces to underscores
            payload = {"username": username, "email": email, "password": password}

            response = requests.post(f"{API_BASE_URL}/register", json=payload)

            response_data = response.json()

            if response.status_code == 201:
                return jsonify({"message": "Registration successful! Please log in."}), 201
            else:
                return jsonify({"message": response_data.get("message", "Registration failed.")}), 400

        except Exception as e:
            return jsonify({"message": "Error processing request", "error": str(e)}), 500

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Handles user login (JSON Input)"""
    if request.method == "POST":
        try:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return jsonify({"message": "Username and password are required"}), 400

            response = requests.post(f"{API_BASE_URL}/login", json=data)
            response_data = response.json()

            if response.status_code == 200:
                session["token"] = response_data.get("access_token")
                return jsonify({"message": "Login successful", "redirect": "/dashboard"}), 200
            else:
                return jsonify({"message": response_data.get("message", "Invalid credentials")}), 401

        except Exception as e:
            return jsonify({"message": "Error processing request", "error": str(e)}), 500

    return render_template("login.html")

@app.route("/logout")
def logout():
    """Logs out the user and clears the session"""
    session.pop("token", None)
    flash("Logged out successfully.", "success")
    return redirect(url_for("login"))

@app.route("/add_task", methods=["POST"])
def add_task():
    """Adds a new task with date & time"""
    if "token" not in session:
        return redirect(url_for("login"))

    try:
        data = request.get_json()
        headers = {"Authorization": f"Bearer {session['token']}"}

        title = data.get("title")
        due_date = data.get("due_date")
        due_time = data.get("due_time")

        if not title or not due_date or not due_time:
            return jsonify({"message": "Title, due_date, and due_time are required"}), 400

        if not validate_time_format(due_time):
            return jsonify({"message": "Invalid time format. Use HH:MM:SS"}), 400

        task_data = {
            "title": title,
            "description": data.get("description", ""),
            "due_date": due_date,
            "due_time": due_time,
            "priority": data.get("priority", "medium"),
        }

        response = requests.post(f"{API_BASE_URL}/tasks", json=task_data, headers=headers)

        if response.status_code == 201:
            return jsonify({"message": "Task created successfully!"}), 201
        else:
            return jsonify({"message": "Failed to create task"}), 400

    except Exception as e:
        return jsonify({"message": "Error processing request", "error": str(e)}), 500

@app.route("/update_task/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Updates an existing task with date & time"""
    if "token" not in session:
        return redirect(url_for("login"))

    try:
        data = request.get_json()
        headers = {"Authorization": f"Bearer {session['token']}"}

        due_time = data.get("due_time")
        if due_time and not validate_time_format(due_time):
            return jsonify({"message": "Invalid time format. Use HH:MM:SS"}), 400

        task_data = {
            "title": data.get("title"),
            "description": data.get("description"),
            "due_date": data.get("due_date"),
            "due_time": due_time,
            "priority": data.get("priority"),
            "status": data.get("status"),
        }

        response = requests.put(f"{API_BASE_URL}/tasks/{task_id}", json=task_data, headers=headers)

        if response.status_code == 200:
            return jsonify({"message": "Task updated successfully!"}), 200
        else:
            return jsonify({"message": "Failed to update task"}), 400

    except Exception as e:
        return jsonify({"message": "Error processing request", "error": str(e)}), 500

@app.route("/get_task/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Fetches and displays task details"""
    if "token" not in session:
        return redirect(url_for("login"))

    headers = {"Authorization": f"Bearer {session['token']}"}
    response = requests.get(f"{API_BASE_URL}/tasks/{task_id}", headers=headers)
    task = response.json() if response.status_code == 200 else {}

    return render_template("task_detail.html", task=task)

@app.route("/delete_task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    """Deletes a task"""
    if "token" not in session:
        return redirect(url_for("login"))

    headers = {"Authorization": f"Bearer {session['token']}"}
    requests.delete(f"{API_BASE_URL}/tasks/{task_id}", headers=headers)

    return redirect("/dashboard")

def validate_time_format(time_str):
    """Validates if the given time string is in HH:MM:SS format"""
    try:
        parts = time_str.split(":")
        return len(parts) == 3 and all(p.isdigit() for p in parts)
    except ValueError:
        return False

if __name__ == "__main__":
    app.run(debug=True)
