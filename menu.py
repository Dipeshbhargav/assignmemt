"""
Menu Module

This module provides the main menu interface for the Employee Management System.
Users can interact with the application through the menu options, which include
adding, deleting, updating employee information, generating reports, and exiting
the application.
"""
from .employee_operations import add_employee, delete_employee, update_employee
from .report_generation import generate_reports

def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. Generate Reports")
        print("5. Exit Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            delete_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            generate_reports()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
def generate_reports_menu():
    while True:
        print("\nGenerate Reports")
        print("1.List of Departments")
        print("2. List of all Employees")
        print("3. Deparment Statistics")
        print("4. Deparment Employee Details")
        print("5. Back to main menu")

        report_choice = input("Enter your choice:")

        if report_choice == '1':
            list_deparment()
        elif report_choice == '2';
             list_employees()
        elif report_choice == '3';
             average_age_and_salary_per_deparment()
        elif report_choice == '4':
            list_employees_per_deparment()
        elif report_choice == '5':
             break
        else:
            print("Invalid choice.please try again.")
if__name__=="__main__":
   main()

        
