from employee_wage import EmployWageComputation
from company_detail import CompanyDetail

class EmployeeWageBuilderObject:
    company=[]
    company.append(CompanyDetail("TCS",20,20,100))
    company.append(CompanyDetail("JIO",20,20,100))
    employee=EmployWageComputation()
    employee.compute_employee_wage(company)
    employee.compute_employee_wage(company)
    