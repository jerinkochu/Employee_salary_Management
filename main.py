
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


# #---------------------------------------------------------
# #----Output Of Permanent and Contract Employee------------

# (.venv) jerinkjohn@Jerins-MacBook-Air Project_Employee_Salary_System % /Users/jerinkjohn/Desktop/PGP_Data_Science_AIML/Project_Employee_Salary_
# System/.venv/bin/python /Users/jerinkjohn/Desktop/PGP_Data_Science_AIML/Project_Employee_Salary_System/main.py


# ---Permanent Employe Details-------
# Holder name = Jerin | ID = ai12 | Role = Analyst | Salary = 50000
# None
# Jerin Total salary is 60000.0


# ---Contract Employe Details-------
# Holder name = Vishnu | ID = ai142 | Role = Engineer | Salary = 55000
# None
# Vishnu Total Salary is 57750.0