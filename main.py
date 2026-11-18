
from PermanentEmployee import PermanentEmployee
from ContractEmployee import ContractEmployee


permanent_employee= PermanentEmployee('Jerin','ai12','Analyst',50000)
contarct_employee=ContractEmployee('Vishnu','ai142','Engineer',55000)

print('---Permanent Employe Details-------')
print(permanent_employee.display_details())
permanent_employee.calculate_salary()
print('\n')
print('---Contract Employe Details-------')
print(contarct_employee.display_details())
contarct_employee.calculate_salary()