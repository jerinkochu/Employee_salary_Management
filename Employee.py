from abc import ABC,abstractmethod                   #import Abstraction method abc : file  ABC : Module 
class Employee:                                      #Construct  Class as Employee 
    def __init__(self,name,id,role,salary):          #initiate Characteristics of an Employee
        self.name=name
        self.id=id
        self.role=role
        self.__salary=salary

    @abstractmethod                                    #Calculate salary have abstractionmethod
    def calculate_salary(self):
        pass                                           #pass : Do nothing now


    @property                                           #property Access Modifier
    def salary(self):                                   #salary is a private attribute
        return self.__salary


    def display_details(self):                          
        print(f"Holder name = {self.name} | ID = {self.id} | Role = {self.role}")