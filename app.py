import streamlit as st

from employee_system import (
    add_employee,
    mark_attendance,
    show_employees,
    search_employee,
    update_salary,
    delete_employee,
    show_attendance
)



st.title("👨‍💼 Employee Attendance System")



menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Add Employee",
        "Mark Attendance",
        "Show Employees",
        "Search Employee",
        "Update Salary",
        "Attendance History",
        "Delete Employee"
    ]
)



if menu=="Add Employee":

    st.header("Add Employee")

    name=st.text_input("Name")
    dept=st.text_input("Department")
    salary=st.number_input(
        "Salary",
        min_value=1
    )


    if st.button("Add"):

        add_employee(
            name,
            dept,
            salary
        )

        st.success("Employee Added")





elif menu=="Mark Attendance":

    st.header("Attendance")

    emp_id=st.number_input(
        "Employee ID",
        min_value=1
    )


    status=st.selectbox(
        "Status",
        ["Present","Absent"]
    )


    if st.button("Submit"):

        mark_attendance(
            emp_id,
            status
        )

        st.success("Attendance Marked")





elif menu=="Show Employees":

    st.header("Employees")

    st.table(
        show_employees()
    )





elif menu=="Search Employee":

    emp_id=st.number_input(
        "Employee ID",
        min_value=1
    )


    if st.button("Search"):

        result=search_employee(emp_id)


        if result:
            st.success(result)

        else:
            st.error("Not Found")





elif menu=="Update Salary":

    emp_id=st.number_input(
        "Employee ID",
        min_value=1
    )

    salary=st.number_input(
        "New Salary",
        min_value=1
    )


    if st.button("Update"):

        if update_salary(emp_id,salary):

            st.success("Updated")

        else:
            st.error("Not Found")





elif menu=="Attendance History":

    emp_id=st.number_input(
        "Employee ID",
        min_value=1
    )


    if st.button("Show"):

        st.table(
            show_attendance(emp_id)
        )





elif menu=="Delete Employee":

    emp_id=st.number_input(
        "Employee ID",
        min_value=1
    )


    if st.button("Delete"):

        if delete_employee(emp_id):

            st.success("Deleted")

        else:
            st.error("Not Found")