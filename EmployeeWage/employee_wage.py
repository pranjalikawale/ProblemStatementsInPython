import math
import random
from company_detail import CompanyDetail

class EmployWageComputation:

    #welcome msg
    print("----Welcome To Employee Wage Problem----")

    #declare constant
    IS_FULL_TIME=1
    IS_PART_TIME=2

    #declare variable
    total_wage=0

    #return fulltime employee working hrs
    def is_full_time(self):
        return 8

    #return parttime employee working hrs
    def is_part_time(self):
        return 4    

    #return zero employee working hrs
    def is_absent(self):
        return 0

    #switcher to select one of the option
    switcher={
        0:is_absent,
        1:is_full_time,
        2:is_part_time,
    }

    #ckeck for employee working hrs
    def get_hour(self):
        #declare variable for attendence
        attendence=math.floor(random.random()*10)%3

        # Get the function from switcher dictionary
        func=self.switcher.get(self,attendence)
        return func

    #return daily empWage
    def get_daily_wage(self,hrs,emp_rate):
        return (hrs*emp_rate)
    
    #compute employ wage
    def compute_employee_wage(self,company_list):

        for company in company_list:
            total_working_day=0
            total_Working_hrs=0 
            hours=0
            employ_rate=company.get_emp_rate()

            #calculate daily employee wage
            while total_Working_hrs<company.get_number_of_hrs() and total_working_day<company.get_number_of_days():
                hours=self.get_hour()
                total_Working_hrs+=hours
                total_working_day+=1
                print(("{0} Employ Wage for day {1} : {2}").format(company.get_company_name(),total_working_day,self.get_daily_wage(hours,employ_rate)))
            
            #calculate mothly employee wage
            self.total_wage=self.get_daily_wage(total_Working_hrs,employ_rate)
            print("{0} Employ Wage for month : {1} \n".format(company.get_company_name(),self.total_wage))

        
