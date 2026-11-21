
from Employee import Employee                           #Parentclass importing to sublass

class ContractEmployee(Employee):                       
    def __init__(self, name, id, role, salary):
        super().__init__(name, id, role, salary) 

    def calculate_salary(self):                         #defining calculate salary from Parent class
        allowance=self.salary+ (self.salary*(0.05))     
        print(f"{self.name} Total Salary is {allowance}")

    def display_details(self):                          #display details from Parent class
      print(f"Holder name = {self.name} | ID = {self.id} | Role = {self.role} | Salary = {self.salary}")
