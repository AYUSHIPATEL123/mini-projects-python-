import random

print("-------------------------------------")
print("| LET'S PLAY THE STONE PAPER SISSOR |")
print("-------------------------------------")
list=["stone","paper","sissor"]
c_score=0
y_score=0
for i in range(1,10):
    computer_gauss=list[random.randint(0,2)]
    your_gauss=list[int(input("Enter Your Gauss (0 for stone /1 for paper /2 for sissor) :"))]

    if computer_gauss==your_gauss:
        print("tied between computer and player...")
        c_score+=1
        y_score+=1
    elif computer_gauss==list[0] and your_gauss==list[1]:
        print("you won......")
        y_score+=2
    elif computer_gauss==list[1] and your_gauss==list[2]:
        print("you won......")
        y_score+=2
    elif computer_gauss==list[2] and your_gauss==list[0]:
        print("you won......")
        y_score+=2
    elif computer_gauss==list[1] and your_gauss==list[0]:
        print("computer won......")
        c_score+=2
    elif computer_gauss==list[2] and your_gauss==list[1]:
        print("computer won......")
        c_score+=2
    elif computer_gauss==list[0] and your_gauss==list[2]:
        print("computer won......")
        c_score+=2

if y_score>c_score:
    print(f"you have been win with {y_score} points.🥳🥳🥳🥳")
elif  y_score==c_score:
    print("match has been tied......👻👻👻")
else:
    print("you have lost the game...!!!🤖🤖🤖🤖")    
