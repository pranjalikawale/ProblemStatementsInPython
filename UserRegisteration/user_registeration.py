import re
from validation_exception import ValidationException

class UserRegisteration:
    NAME_PATTERN=r'^[A-Z][a-z]{2,20}'
    MOBILE_PATTERN=r'[0-9]{2}[ ][0-9]{10}$'
    EMAIL_PATTERN=r'^[a-z]{1}[a-z0-9]{1,}[.|_|+|-]?[a-z0-9]{1,}?@[a-z0-9]{1,}[.][a-z]{2,4}([.][a-z]{2})?$'
    PASSWORD_PATTERN=r'(?=.*?[A-Z])(?=.*?[\d])(?=.*?[^#|?|!|@|$|%|^|&|*|-]*[^#|?|!|@|$|%|^|&|*|-][#|?|!|@|$|%|^|&|*|-]*$)[a-zA-Z0-9#^?!@$%^&*-]{8,}' 

    #check for name validation
    def check_name_validation(self,name):
        try:
            self.pattern=re.match(self.NAME_PATTERN,name)
            if self.pattern[0]==name:
                print("Valid name")
                return True
        except:
            raise ValidationException("Invalid Name")

    #check for mobile validation
    def check_mobile_validation(self,mobile):
        try:
            self.pattern=re.match(self.MOBILE_PATTERN,mobile)
            if self.pattern[0]==mobile:
                print("Valid Mobile Number")
                return True
        except:
            raise ValidationException("Invalid Mobile Number")

    #check for email validation
    def check_email_validation(self,email):
        try:
            self.pattern=re.match(self.EMAIL_PATTERN,email)
            if self.pattern[0]==email:
                print("Valid Email Address")
                return True
        except:
            raise ValidationException("Invalid Email Address")
        return False

    
    #check for password validation
    def check_password_validation(self,password):
        try:
            self.pattern=re.match(self.PASSWORD_PATTERN,password)
            if self.pattern[0]==password:
                print("Valid Password")
                return True
        except:
            raise ValidationException("Invalid Password")
    

       
