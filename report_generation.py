"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""

def generate_reports():
    """
    Generate Reports Function

    This function generates various reports based on employee data, such as:
    - List of departments
    - List of all employees with ID, full name, and department
    - List of all departments with the average age and salary of employees
    - List of employees in each department with ID, full name, date of birth, salary,
      and total salary for department's employees
    """

departments = get_departments()
    employees = get_employees()

    print("List of Departments:")
    for department in departments:
        print(department)

    print("\nList of Employees:")
    for employee in employees:
        print(f"ID: {employee['id']}, Name: {employee['name']}, Department: {employee['department']}")

    print("\nList of Departments with Average Age and Salary:")
    for department in departments:
        avg_age, avg_salary = calculate_department_stats(employees, department)
        print(f"Department: {department}, Average Age: {avg_age}, Average Salary: {avg_salary}")

    print("\nEmployees in Each Department:")
    for department in departments:
        print(f"\nDepartment: {department}")
        department_employees = [employee for employee in employees if employee['department'] == department]
        total_salary = sum(employee['salary'] for employee in department_employees)
        for employee in department_employees:
            print(
                f"ID: {employee['id']}, Name: {employee['name']}, Date of Birth: {employee['dob']}, Salary: {employee['salary']}, Total Salary for Department: {total_salary}")


def get_departments():
    return ["Analyst", "Engineer", "Manager"]


def get_employees():
    return [
        {"id": 1, "name": "Mukul Sharma", "department": "Manager", "dob": "1980-05-15", "salary": 160000},
        {"id": 2, "name": "Simran Kaur", "department": "Engineer", "dob": "1975-12-20", "salary": 90000},
        {"id": 3, "name": "William Smith", "department": "Analyst", "dob": "1990-08-10", "salary": 75000},
    ]


def calculate_department_stats(employees, department):
    department_employees = [employee for employee in employees if employee['department'] == department]
    if len(department_employees) == 0:
        return 0, 0
    avg_age = sum(get_age(employee['dob']) for employee in department_employees) / len(department_employees)
    avg_salary = sum(employee['salary'] for employee in department_employees) / len(department_employees)
    return avg_age, avg_salary


def get_age(date_of_birth):
    import datetime
    today = datetime.date.today()
    dob = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age
