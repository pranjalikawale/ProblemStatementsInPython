import random

head=0
tail=0

flipCoinCounter=int(input("Enter the number of time coin flip"))
coinFlipped=flipCoinCounter

while coinFlipped>0:
    if random.random()<0.5 :
        tail+=1
    else:
        head+=1
    coinFlipped-=1 

headPercentage=(head/flipCoinCounter)*100
tailPercentage=(tail/flipCoinCounter)*100

print("{0} is head percentage ".format(headPercentage))
print("{0} is tail percentage ".format(tailPercentage))      