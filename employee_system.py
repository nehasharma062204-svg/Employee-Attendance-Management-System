import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path


# ---------------------------------
# LOAD ENV FILE
# ---------------------------------

ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)


DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


if not DB_HOST or not DB_USER or not DB_PASSWORD or not DB_NAME:
    raise ValueError("❌ .env variables missing")



# ---------------------------------
# DATABASE CONNECTION
# ---------------------------------

def get_connection():

    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )




# ---------------------------------
# ADD EMPLOYEE
# ---------------------------------

def add_employee(name, dept, salary):

    conn = get_connection()
    cursor = conn.cursor()


    query = """
    INSERT INTO employees
    (name, department, salary)
    VALUES (%s,%s,%s)
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
    (emp_id,date,time,status)
    VALUES(%s,%s,%s,%s)
    """


    cursor.execute(
        query,
        (
            emp_id,
            now.date(),
            now.time(),
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
        "SELECT * FROM employees WHERE emp_id=%s",
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
        SET salary=%s
        WHERE emp_id=%s
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
        SELECT date,time,status
        FROM attendance
        WHERE emp_id=%s
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
        "DELETE FROM employees WHERE emp_id=%s",
        (emp_id,)
    )


    conn.commit()


    deleted = cursor.rowcount


    cursor.close()
    conn.close()


    return deleted




# ---------------------------------
# TERMINAL TEST MENU
# ---------------------------------

if __name__ == "__main__":

    print("✔ Employee System Backend Running")

    while True:

        print("\n----- MENU -----")
        print("1. Add Employee")
        print("2. Show Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Mark Attendance")
        print("7. Show Attendance")
        print("8. Exit")


        choice = input("Enter choice: ")


        if choice=="1":

            name=input("Name: ")
            dept=input("Department: ")
            salary=int(input("Salary: "))

            add_employee(
                name,
                dept,
                salary
            )

            print("✔ Added")



        elif choice=="2":

            for row in show_employees():
                print(row)



        elif choice=="3":

            emp=int(input("Employee ID: "))

            print(
                search_employee(emp)
            )



        elif choice=="4":

            emp=int(input("ID: "))
            salary=int(input("New Salary: "))

            update_salary(
                emp,
                salary
            )

            print("✔ Updated")



        elif choice=="5":

            emp=int(input("ID: "))

            delete_employee(emp)

            print("✔ Deleted")



        elif choice=="6":

            emp=int(input("ID: "))
            status=input("Present/Absent: ")

            mark_attendance(
                emp,
                status
            )

            print("✔ Attendance marked")



        elif choice=="7":

            emp=int(input("ID: "))

            for row in show_attendance(emp):
                print(row)



        elif choice=="8":
            break


        else:
            print("Invalid choice")