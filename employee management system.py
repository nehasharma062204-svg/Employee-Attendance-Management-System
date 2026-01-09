import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

# -------------------------------------------------
# LOAD ENV FILE (WINDOWS SAFE)
# -------------------------------------------------
ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Safety check
if not DB_HOST or not DB_USER or not DB_PASSWORD or not DB_NAME:
    raise ValueError("❌ .env file not loaded or variables missing")

# -------------------------------------------------
# DATABASE CONNECTION
# -------------------------------------------------
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = conn.cursor()
print("✔ Database Connected Successfully\n")

# -------------------------------------------------
# ADD EMPLOYEE
# -------------------------------------------------
def add_employee():
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")

    try:
        salary = int(input("Enter Salary: "))
        if salary <= 0:
            print("❌ Salary must be greater than 0\n")
            return
    except ValueError:
        print("❌ Salary must be a number\n")
        return

    query = """
    INSERT INTO employees (name, department, salary)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (name, dept, salary))
    conn.commit()
    print("✔ Employee Added Successfully\n")

# -------------------------------------------------
# MARK ATTENDANCE
# -------------------------------------------------
def mark_attendance():
    try:
        emp_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("❌ Invalid Employee ID\n")
        return

    status = input("Present / Absent: ").capitalize()
    if status not in ["Present", "Absent"]:
        print("❌ Invalid Status\n")
        return

    now = datetime.now()

    query = """
    INSERT INTO attendance (emp_id, date, time, status)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (emp_id, now.date(), now.time(), status))
    conn.commit()
    print("✔ Attendance Marked\n")

# -------------------------------------------------
# SHOW ALL EMPLOYEES
# -------------------------------------------------
def show_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\nEMP_ID | NAME | DEPARTMENT | SALARY")
    print("----------------------------------")
    for r in rows:
        print(r)
    print()

# -------------------------------------------------
# SEARCH EMPLOYEE
# -------------------------------------------------
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("❌ Invalid ID\n")
        return

    cursor.execute("SELECT * FROM employees WHERE emp_id=%s", (emp_id,))
    row = cursor.fetchone()

    if row:
        print("✔ Employee Found:", row, "\n")
    else:
        print("❌ Employee Not Found\n")

# -------------------------------------------------
# UPDATE SALARY
# -------------------------------------------------
def update_salary():
    try:
        emp_id = int(input("Enter Employee ID: "))
        new_salary = int(input("Enter New Salary: "))
    except ValueError:
        print("❌ Invalid input\n")
        return

    cursor.execute(
        "UPDATE employees SET salary=%s WHERE emp_id=%s",
        (new_salary, emp_id)
    )
    conn.commit()

    if cursor.rowcount:
        print("✔ Salary Updated\n")
    else:
        print("❌ Employee Not Found\n")

# -------------------------------------------------
# SHOW ATTENDANCE
# -------------------------------------------------
def show_attendance():
    try:
        emp_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("❌ Invalid ID\n")
        return

    cursor.execute(
        "SELECT date, time, status FROM attendance WHERE emp_id=%s",
        (emp_id,)
    )
    rows = cursor.fetchall()

    if not rows:
        print("❌ No attendance records found\n")
        return

    print("\nDATE | TIME | STATUS")
    print("-------------------")
    for r in rows:
        print(r)
    print()

# -------------------------------------------------
# DELETE EMPLOYEE
# -------------------------------------------------
def delete_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("❌ Invalid ID\n")
        return

    cursor.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
    conn.commit()

    if cursor.rowcount:
        print("✔ Employee Deleted\n")
    else:
        print("❌ Employee Not Found\n")

# -------------------------------------------------
# MAIN MENU
# -------------------------------------------------
while True:
    print("----- Employee Attendance System -----")
    print("1. Add Employee")
    print("2. Mark Attendance")
    print("3. Show Employees")
    print("4. Search Employee")
    print("5. Update Salary")
    print("6. Show Attendance History")
    print("7. Delete Employee")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        show_employees()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        update_salary()
    elif choice == "6":
        show_attendance()
    elif choice == "7":
        delete_employee()
    elif choice == "8":
        print("Program Ended")
        break
    else:
        print("❌ Invalid Choice\n")

# -------------------------------------------------
# CLOSE CONNECTION
# -------------------------------------------------
cursor.close()
conn.close()
print("✔ Database Connection Closed")