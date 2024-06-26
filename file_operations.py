"""
File Operations Module

This module provides functions for reading from and writing to the text file
that stores employee data.
"""
def read_employees():
    """
    Read Employees Function

    This function reads employee data from the text file and returns it.

    Returns:
        list: A list containing employee data read from the text file.
    """
    employee_data = []
     with open('employees.txt', 'r') as file:
        for line in file:
            employee = line.strip()
            employee_data.append(employee)
    return employee_data

    

def write_employees():
    """
    Write Employees Function

    This function writes employee data to the text file.

    Parameters:
        employees_data (list): A list containing employee data to be written to the text file.
    """
    with open('employees.txt','w')as file:
        for employee in employees_data:
            file.write(f"{employee}\n")
