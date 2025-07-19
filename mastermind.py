import random

player1=0
player2=0
player=1
for i in range(2):
    r_num=random.randint(1000,9999)
    n=input("enter a 4 digite number :")
    
    if r_num==n:
        print("you are mastermind.........!!!!!")
    else:
        ctr=1
        while n!=r_num:
            ctr+=1
            r_num=str(r_num)
            correct=[]
            count=0
            for i in range(4):
                if n[i]==r_num[i]:
                    count+=1
                    correct.append(n[i])
            if count<4 and count!=0:
                print(f"you don't get the number,but you got {count} correct digites and \n and thode digits are : {correct}")
                n=input("enter your next choice :")
            elif count==0:
                print(" you dont find any of the digits")
                n=input("enter your next choice :")
        if n==r_num:
            print("you are master mind")
            print(f"you get in int the {ctr} tries")
            if i==0:
                player1=ctr
            else:
                player2=ctr
        
if player2<player1:
    print("player 2 wins the game")
elif player1<player2:
    print("player 1 is the winner")
else:
    print("game tied...")                                