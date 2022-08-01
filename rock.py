import random
def solve():
    print("rules for the game are")
    print("enter 1 for Rock")
    print("enter 2 for paper")
    print("enter 3 for scissor")
    
    print("enter a choice")
    n=int(input())
    
            
    b=True
    while( b):
        
        a=0
        m=["rock","paper","scissor"]
        s=random.choice(m)
        if s=="rock":
            a=1
        elif s=="paper":
            a=2
        else:
            a=3
        if a==1 and n==1 or a==2 and n==2 or a==3 and n==3:
            print("computer choice is ",s)
            print("draw")
        if n==1 and a==2:
            print("computer choice is ",s)
            print("computer win")
        if n==1 and a==3:
            print("computer choice is",s)
            print("you win")
        if n==2 and a==1:
            print("computer choice is",s)
            print("computer win")
        if n==2 and a==3:
            print("computer choice is ",s)
            print("you win") 
        if n==3 and a==1:
            print("computer choice is ",s)
            print("computer win")
        if n==3 and a==2:
            print("computer choice is",s)
            print("you win")
        print("do u want to continue Y/N")
        con=input()
        if con =="n":
            break
        else:
            solve()
        
   
        
        

solve()            




 
    




