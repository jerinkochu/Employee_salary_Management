
from PermanentEmployee import PermanentEmployee         #Importing Subclass (PermanentEmployee)
from ContractEmployee import ContractEmployee           #Importing Subclass (ContractEmployee )


permanent_employee= PermanentEmployee('Jerin','ai12','Analyst',50000)       
contarct_employee=ContractEmployee('Vishnu','ai142','Engineer',55000)

#Permanent Employee Details Display
print('---Permanent Employe Details-------')
print(permanent_employee.display_details())             #import Display details from the ParentClass
permanent_employee.calculate_salary()                   #Calculate Salary of PermanentEmployee
print('\n')
#Contract Employee Details Display
print('---Contract Employe Details-------')
print(contarct_employee.display_details())
contarct_employee.calculate_salary()