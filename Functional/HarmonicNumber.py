def harmonicNumber(rangeOfNumber):
    harmonicNumber=0

    for i in range(1,rangeOfNumber+1):
        harmonicNumber+=1/i

    print(harmonicNumber)

try:
    rangeForHarmonicNumber=int(input("Enter number"))
    harmonicNumber(rangeForHarmonicNumber)
except:
    print("Plz enter a valid number") 