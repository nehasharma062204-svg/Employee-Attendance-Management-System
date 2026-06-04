import sqlite3
from datetime import datetime


# ---------------------------------
# DATABASE CONNECTION
# ---------------------------------

def get_connection():
    return sqlite3.connect("attendance.db")


# ---------------------------------
# ADD EMPLOYEE
# ---------------------------------

def add_employee(name, dept, salary):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO employees
    (name, department, salary)
    VALUES (?, ?, ?)
    """

    cursor.execute(
        query,
        (name, dept, salary)
    )

    conn.commit()

    cursor.close()
    conn.close()


# ---------------------------------
# MARK ATTENDANCE
# ---------------------------------

def mark_attendance(emp_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now()

    query = """
    INSERT INTO attendance
    (emp_id, date, time, status)
    VALUES (?, ?, ?, ?)
    """

    cursor.execute(
        query,
        (
            emp_id,
            str(now.date()),
            str(now.time()),
            status
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


# ---------------------------------
# SHOW EMPLOYEES
# ---------------------------------

def show_employees():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees"
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


# ---------------------------------
# SEARCH EMPLOYEE
# ---------------------------------

def search_employee(emp_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data


# ---------------------------------
# UPDATE SALARY
# ---------------------------------

def update_salary(emp_id, new_salary):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE employees
        SET salary=?
        WHERE emp_id=?
        """,
        (
            new_salary,
            emp_id
        )
    )

    conn.commit()

    updated = cursor.rowcount

    cursor.close()
    conn.close()

    return updated


# ---------------------------------
# SHOW ATTENDANCE
# ---------------------------------

def show_attendance(emp_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT date, time, status
        FROM attendance
        WHERE emp_id=?
        """,
        (emp_id,)
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


# ---------------------------------
# DELETE EMPLOYEE
# ---------------------------------

def delete_employee(emp_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    conn.commit()

    deleted = cursor.rowcount

    cursor.close()
    conn.close()

    return deleted


# ---------------------------------
# CREATE TABLES
# ---------------------------------

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        department TEXT,
        salary INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id INTEGER,
        date TEXT,
        time TEXT,
        status TEXT
    )
    """)

    conn.commit()

    cursor.close()
    conn.close()


create_tables()


if __name__ == "__main__":
    print("✔ Employee System Backend Running")