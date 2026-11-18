from Employee import Employee


class PermanentEmployee(Employee):
    def __init__(self, name, id, role, salary):
        super().__init__(name, id, role, salary)


    def calculate_salary(self):
        allowance=self.salary+(self.salary*(0.2))
        print(f"{self.name} Total salary is {allowance}")

    def display_details(self):
        print(f"Holder name = {self.name} | ID = {self.id} | Role = {self.role} | Salary = {self.salary}")

