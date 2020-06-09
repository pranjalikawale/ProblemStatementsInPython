import math

class QuadraticEquation:
    #calculate delta
    def calculate_delta(self,parameter_1,parameter_2,parameter_3):
        return ((parameter_2**2) - (4*parameter_1*parameter_3))

    #find root for quadratic equation
    def calculate_root(self,parameter_1,parameter_2,parameter_3): 
        
        #call calculate_delta
        delta=self.calculate_delta(parameter_1,parameter_2,parameter_3)
        
        #calculate root
        root_1=(-parameter_2-math.sqrt(delta))/(2*parameter_1)
        root_2=(-parameter_2+math.sqrt(delta))/(2*parameter_1)

        #print root
        print('The roots are {0} and {1}'.format(root_1,root_2))

#main
while True:
    try:
        #enter input
        parameter_1=int(input("Enter a value"))
        parameter_2=int(input("Enter b value"))
        parameter_3=int(input("Enter c value"))
        #create object
        equation=QuadraticEquation()
        #invoke calculate_root method
        equation.calculate_root(parameter_1,parameter_2,parameter_3)
        break
    except ValueError:
        print("Plz enter valid equation") 
