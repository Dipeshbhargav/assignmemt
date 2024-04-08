"""
# Employee Operations Module
class Employee:
    def__init__(self, id, first_name, last_name, date_of_birth, start_year, position, salary):
       self.id = id
       self.first_name = first_name
       self.last_name = last_name
       self.date_of_birth = date_of_birth
       self.start_year = start_year
       self.position = position
       self.salary = salary
employees = [
    Employee(1, 'Simran', 'Kaur', '2000-04-05', 2018, 'Manager', 80000),
    Employee(2, 'Mukul', 'Sharma', '1999-03-04', 2014, 'Developer', 85000),
    Employee(3, 'Ivneet', 'Randhava', '2000-04-05', 2018, 'Designer', 75000),
    
def add_employee():
    #Add Employee function
    #input details for a new employee and adds the new employee
    id = int(input("please enter the ID for the new employee:"))
    firstName = input("please enter the employee's firstname")
    last_name = input("please enter the employee's lastname")
    date_of_birth = input("please enter the employee's date of birth in YYYY/MM/DD")
    start_of_year = int(input("please enter the employee's starting year")
    position = input("please enter the employee's position")
    salary = float(input("please enter the employee's salary")
    new_employee = Employee(id, first_name, last_name, date_of_birth, start_year, position, salary)
    employees.append(new_employee)
    print(f"Employee {new_employee.first_name} {new_employee.last_name} added to the system.")
    
def delete_employee():
    # Delete Employee Function
    # input the ID of the employee to be deleted and 
    # removes the employee from the system.
    id = int(input("Enter the ID of the employee to be deleted: "))
    for employee in employees:
        if employee.id == id:
            employees.remove(employee)
            print(f"Employee with ID {id} deleted from the system.")
            return
    print(f"No employee with ID {id} found in the system.")
    
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


