import random

player1=0
player2=0
player=1
for i in range(2):
    r_num=random.randint(1000,9999)  #genrate random 4 digit number
    n=input("enter a 4 digite number :") #enter th 4 dig number
    
    if r_num==n:        #first try compare only one time
        print("you are mastermind.........!!!!!")
    else:
        ctr=1 #count the tries of player
        while n!=r_num:     
            ctr+=1
            r_num=str(r_num) #convert it to string
            correct=[] #to store currect digite for each try
            count=0  #to count no of correct digite for each try
            for i in range(4): 
                if n[i]==r_num[i]:
                    count+=1
                    correct.append(n[i])
            if count<4 and count!=0: # if any digite is found
                print(f"you don't get the number,but you got {count} correct digites and \n and those digits are : {correct}")
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
