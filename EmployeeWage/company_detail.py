class CompanyDetail:
    #initialize class variable
    def __init__(self,company_name,emp_rate,number_of_days,number_of_hrs):
        self.company_name=company_name
        self.emp_rate=emp_rate
        self.number_of_days=number_of_days
        self.number_of_hrs=number_of_hrs    

    def get_company_name(self):
        return self.company_name

    def get_emp_rate(self):
        return self.emp_rate

    def get_number_of_days(self):
        return self.number_of_days

    def get_number_of_hrs(self):
        return self.number_of_hrs