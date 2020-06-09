import math

def primeFactor(number):
    while number%2==0:
        print(2)
        number/=2

    for i in range(3,int(math.sqrt(number))+1,2):
        while number%i==0:
            print(i)
            number/=i

    if number>2:
        print(number)        
    
try:
    number=int(input("Enter number"))
    primeFactor(number)
except:
    print("Plz enter a valid number") 