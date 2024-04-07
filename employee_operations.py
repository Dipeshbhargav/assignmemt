"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""

def add_employee():

    firstName = input("please enter the employee's firstname")
    last_name = input("please enter the employee's lastname")
    date_of_birth = input("please enter the employee's date of birth in YYYY/MM/DD")
    start_of_year = input("please enter the employee's starting year")
    position = input("please enter the employee's position")
    salary = input("please enter the employee's salary")

    """
    Add Employee function
    
    This function prompts the user to input details for a new employee and adds the employee to the system.
    
    """
def delete_employee():

    position = int(input("please enter employees position"))
    firstName = int(input("please enter the employees firstname"))

    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """

def update_employee():
    """
    firstname

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    ""
