# 📌 Todo App - Task Management System

## 📋 Overview
This **Todo App** is a simple, intuitive, and interactive task management system that allows users to **register, log in, create tasks, update tasks, delete tasks, and view task details** efficiently. The UI is modern and user-friendly, making it fun and easy to manage daily tasks. 🚀

---

## ✨ Features
✅ **User Registration & Login** - Secure authentication system
✅ **Task Creation** - Add tasks with a title, description, due date, and priority
✅ **Task Dashboard** - View all tasks in a structured format
✅ **Edit & Delete Tasks** - Modify or remove tasks anytime
✅ **Task Details** - View individual task details with due date and time
✅ **Responsive UI** - Works seamlessly on different screen sizes

---

## 🖥️ User Interface

### **Home Page**
![image](https://github.com/user-attachments/assets/84f775d0-127e-4954-a2a9-5b4708bd67dd)
![image](https://github.com/user-attachments/assets/0400ceab-5456-44d5-8305-09caccd747ee)
![image](https://github.com/user-attachments/assets/62470a76-86da-4756-b0dc-83f94f277194)

### **Registration** 📝
![image](https://github.com/user-attachments/assets/6a6bb4d1-6688-4868-bcc4-8a4a356ff47a)

### **Login** 🔐
![image](https://github.com/user-attachments/assets/2168186d-2efd-418a-b382-8d5785fedfc0)

### **Task Dashboard** 📌
![image](https://github.com/user-attachments/assets/2666a6c8-9937-4369-a701-e996139b2790)

### **Task Created** ✅
![image](https://github.com/user-attachments/assets/c84eff95-3e47-4d48-9e11-b9474f3a6f31)

### **View Task Details** 🔍
![image](https://github.com/user-attachments/assets/50494279-dee9-4e1f-85b5-2ba5811922d3)

---

## 🛠️ Setup & Installation

### **Prerequisites**
Ensure you have **Python 3.x** and `pip` installed.

### **1️⃣ Clone the Repository**
```bash
$ git clone https://github.com/your-repository/todo-app.git
$ cd todo-app
```

### **2️⃣ Install Dependencies**
```bash
$ pip install -r requirements.txt
```

### **3️⃣ Set up Environment Variables**
Create a `.env` file in the root directory and add:
```
JWT_SECRET_KEY=your_secret_key_here
```

### **4️⃣ Run the Application**
```bash
$ python app.py
```

The app will be accessible at: **[https://donezo-c2n3.onrender.com/]** 🎉

---

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|----------|--------------|
| `POST` | `/register` | Register a new user |
| `POST` | `/login` | Authenticate user |
| `GET` | `/dashboard` | View all tasks |
| `POST` | `/add_task` | Add a new task |
| `PUT` | `/update_task/<task_id>` | Update an existing task |
| `DELETE` | `/delete_task/<task_id>` | Delete a task |
| `GET` | `/get_task/<task_id>` | View details of a specific task |

---

## 📌 Technologies Used
- **Flask** - Backend framework 🐍
- **HTML, CSS** - Frontend design 🎨
- **JavaScript** - Dynamic UI & API interactions ⚡
- **Bootstrap** - Responsive design 📱
- **SQLite/PostgreSQL** - Database 📊

---

## ✉️ Contact & Support
If you face any issues or have suggestions, feel free to **open an issue** or **contact us** at:
📧 **shubhamchaudhary@pw.live**

---

⭐ **Don't forget to give this repository a star if you find it useful!** ⭐
