import random
n=input("Enter Your Name:")
t=0
s=0
while True:
    A=['Rock','Paper','Scissor']
    comp=random.choice(A).lower()
    r=input("Choose Rock,Paper,Scissor or Exit(if you want to quit)").lower()
    if(r not in ['rock','paper','scissor','exit']):
        print("Try Again")
        continue
    elif(r=='exit'):
        break
    print("Your Choice:",r)
    print("Computer's Choice:",comp)
    if(comp=="rock"):
        if(r=="paper"):
            print("You Won")
            t=t+1
        elif(r=="scissor"):
            print("You Lost")
            s=s+1
    elif(comp=="paper"):
        if(r=="rock"):
            print("You Lost")
            s=s+1
        elif(r=="scissor"):
            print("You Won")
            t=t+1
    elif(comp=="scissor"):
        if(r=="rock"):
            print("You Won")
            t=t+1
        elif(r=="paper"):
            print("You Lost")
            s=s+1
    if(comp==r):
        print("It's a Tie")
print("Your Score:",t)
print("Computer's Score:",s)
if(t>s):
    print("Congratulations! {} You Won".format(n))
else:
    print("Unfortunately! {} You Lost".format(n))
       
