# 👨‍💼 Employee Attendance Management System (Python + MySQL)

## 📌 Project Overview
The **Employee Attendance Management System** is a **menu-driven Python application** that uses **MySQL** as the backend database to manage employee records and their attendance.

This project demonstrates **core backend development skills**, including database design, CRUD operations, and Python–MySQL integration. It is suitable for **college projects, GitHub portfolios, and beginner backend roles**.

---

## 🎯 Project Objectives
- Add and manage employee records
- Mark daily attendance (Present / Absent)
- View attendance history of employees
- Update employee salary
- Delete employees and related attendance
- Use MySQL for persistent data storage

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Database:** MySQL  
- **Libraries Used:**
  - mysql-connector-python
  - python-dotenv (optional)
- **Tools:**
  - MySQL Workbench
  - VS Code
  - PowerShell / Terminal

---

## 📂 Project Structure
```

employee attendance management/
│── attendance_system.py
│── .env
│── .gitignore
│── README.md

````

---

## 🗄️ Database Schema

### Employees Table
| Column | Type |
|------|------|
emp_id | INT (Primary Key)  
name | VARCHAR  
department | VARCHAR  
salary | INT  

### Attendance Table
| Column | Type |
|------|------|
att_id | INT (Primary Key)  
emp_id | INT (Foreign Key)  
date | DATE  
time | TIME  
status | ENUM (Present, Absent)  

---

## 🧾 SQL Setup

Run the following SQL commands in **MySQL Workbench**:

```sql
CREATE DATABASE attendance_db;
USE attendance_db;

CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary INT
);

CREATE TABLE attendance (
    att_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    date DATE,
    time TIME,
    status ENUM('Present','Absent'),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id) ON DELETE CASCADE
);
````

---

## 🔐 Environment Variables (Optional & Secure)

Create a `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=attendance_db
```

⚠️ Do NOT upload `.env` to GitHub.

### `.gitignore`

```
.env
__pycache__/
*.pyc
```

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install mysql-connector-python python-dotenv
```

### 2️⃣ Run the application

```bash
python attendance_system.py
```

---

## 📋 Features

* Add employee details
* Mark attendance with date and time
* Display all employees
* Search employee by ID
* Update employee salary
* View attendance history
* Delete employee records
* Menu-driven user interface

---

## 🧠 Skills Demonstrated

* Python programming
* MySQL database integration
* SQL queries (CRUD)
* Relational database design
* Error handling and validation
* Menu-driven application logic
* Secure credential handling
* Git & GitHub usage

---

## 📌 Resume Description (Copy–Paste)

**Employee Attendance Management System**

* Developed a Python–MySQL based system to manage employee records and attendance
* Implemented CRUD operations with relational database design
* Built a menu-driven console application
* Applied secure database practices and GitHub-ready project structure

---

## 🔮 Future Enhancements

* User login and authentication
* Monthly attendance reports
* Export attendance to CSV
* GUI using Tkinter
* Web version using Flask/Django

---

## 👤 Author

Neha Sharma