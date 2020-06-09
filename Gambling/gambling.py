import random

#calculate gambling wining and losing probability
def gambling(stake,goal,trials):
    
    #local variable
    bet=0
    win=0
    lose=0

    #loop until counter reach to trials
    for counter in range(1,trials+1):
        money=stake

        #loop until money reach to 0 and goal value 
        while money>0 and money<goal:
            bet=+1
            # increment money by one if random value is less than 0.5 else decrement money by one
            if random.random()<0.5:
                money+=1
            else:
                money-=1

        #check if money equal to goal then win else lose
        if money==goal:
            win+=1
        else:
            lose+=1    

    #calculate wining and losing percentage
    wining_percentage=(win/trials)*100
    losing_percentage=(lose/trials)*100

    #print wining_percentage and losing_percentage
    print(("{0} win and {1} lose of {2} trials").format(win,lose,trials))
    print("Wining percentage {0}".format(wining_percentage))
    print("Losing percentage {0}".format(losing_percentage))

#main
#input from user
stake=int(input("Enter stake "))
goal=int(input("Enter goal "))
trials=int(input("Enter trials "))

#function call to gambling()
gambling(stake,goal,trials)
