def powerOfTwo(rangeOfNumber):
    powerOfNumber=2
    i=1
    while i<rangeOfNumber+1:
        print(powerOfNumber*i)
        i+=1

try:
    rangeForTable=int(input("Enter number"))
    powerOfTwo(rangeForTable)
except:
    print("Plz enter a valid number") 