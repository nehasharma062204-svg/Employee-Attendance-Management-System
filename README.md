# 👨‍💼 Employee Attendance Management System

A Python based Employee Attendance Management System using MySQL database and Streamlit web interface.

The project contains a separate backend file and frontend file.

## Features

* Add new employee
* View all employees
* Search employee by ID
* Update employee salary
* Delete employee
* Mark employee attendance
* View attendance history
* MySQL database integration
* Streamlit web UI

## Technologies Used

* Python
* Streamlit
* MySQL
* mysql-connector-python
* python-dotenv

## Project Structure

```text
Employee-Attendance-System/

│
├── employee_system.py
│     └── Database connection
│     └── CRUD operations
│     └── Backend logic
│
├── app.py
│     └── Streamlit frontend
│
├── requirements.txt
│
├── README.md
│
└── .env
```

## Setup

### 1. Clone Repository

```bash
git clone your-repository-link
```

Go inside project:

```bash
cd Employee-Attendance-System
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=employee_db
```

---

## Database Setup

Create database:

```sql
CREATE DATABASE employee_db;
```

Create employee table:

```sql
CREATE TABLE employees(
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary INT
);
```

Create attendance table:

```sql
CREATE TABLE attendance(
    id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    date DATE,
    time TIME,
    status VARCHAR(20)
);
```

---

## Run Terminal Version

```bash
python employee_system.py
```

This runs the backend through terminal menu.

---

## Run Streamlit Version

```bash
streamlit run app.py
```

The application opens in browser.

---

## Application Flow

User

↓

Streamlit Interface (`app.py`)

↓

Backend Functions (`employee_system.py`)

↓

MySQL Database

---

## Deployment

This project can be deployed using Streamlit Community Cloud.

Steps:

1. Upload project to GitHub
2. Open Streamlit Cloud
3. Select repository
4. Choose `app.py`
5. Deploy

---

## Author

Neha Sharma
