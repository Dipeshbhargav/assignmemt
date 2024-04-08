"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""

def add_employee():
    id = int(input("please enter the ID for the new employee:")
    firstName = input("please enter the employee's firstname")
    last_name = input("please enter the employee's lastname")
    date_of_birth = input("please enter the employee's date of birth in YYYY/MM/DD")
    start_of_year = int(input("please enter the employee's starting year")
    position = input("please enter the employee's position")
    salary = float(input("please enter the employee's salary")

    """
    Add Employee function
    
    This function prompts the user to input details for a new employee and adds the employee to the system.
    
    """
def delete_employee():

    {"id": "001", "first_name": "John", "last_name": "Doe"}
    {"id": "002", "first_name": "Alice", "last_name": "Smith"}
    {"id": "003", "first_name": "Bob", "last_name": "Johnson"} 
    {"id": "004", "first_name": "Mukul", "last_name": "Sharma"}
    {"id": "005", "first_name": "Sophia", "last_name": "Davis"}
    {"id": "006", "first_name": "Michael", "last_name": "Brown"}
    
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """

def update_employee():
    id = int(input(" enter the ID  of the employee to be update:")
    for employee in employees:
        if employee.id == id:
           first_name = input("enter the new first name for the employee:")
           last_name = input ("enter the new last name for the employee:")
           date_of_birth = input("enter the new date of birth for the employee(YYY/MM/DD):")
           start_of_year = int(input("enter the new start of year for the employee:"))
           position= input("enter the new position for the employee:")
           salary = float(input("enter the new salary for the employee:"))

           employee.first_name= first_name
           employee.last_name=last_name
           employee.date_of_birth= date_of_birth
           employee.start_of_year= start_of_year
           employee.position= position
           employee.salary = salary

           print(f"employee with ID {ID} updated.")
           return
     print(f"No employee with ID{id} found in the system.")


#update employee function
   This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.


