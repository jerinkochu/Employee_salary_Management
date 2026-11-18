from abc import ABC,abstractmethod
class Employee:
    def __init__(self,name,id,role,salary):
        self.name=name
        self.id=id
        self.role=role
        self.__salary=salary

    @abstractmethod
    def calculate_salary(self):
        pass


    @property
    def salary(self):
        return self.__salary


    def display_details(self):
        print(f"Holder name = {self.name} | ID = {self.id} | Role = {self.role}")