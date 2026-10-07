
import random


computer = random.choice([1,-1,0])
youstr = input("Enter your choice : ")
youDict = { "s" : 1,"w" : -1, "g" : 0}
reverseDict = { 1 : "snake", -1 : "water", 0 : "gun"}
you = youDict[youstr]

print( f"You choose {reverseDict[you]} and Computer choose {reverseDict[computer]}")

if ((computer - you) == -2 or (computer -you) == 1 ):
    print("You win, Contratulations!!")
else:
    print("Ops! You loose")


'''
if( you == computer):
    print("It's a Draw!")

else:
    if(computer == -1 and you == 0): -1
        print ("You loose")
    elif(computer == -1 and you == 1): -2
        print ("You win")
    elif(computer == 1 and you == -1): 2
        print ("You loose")
    elif(computer == 1 and you == 0 ): 1
        print ("You win") 
    elif(computer == 0 and you == -1): 1
        print("You win")
    elif(computer == 0 and you == 1): -1
        print("You loose")
    else:
        print("Something went wrong!")
        '''
