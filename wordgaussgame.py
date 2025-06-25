import random


print("-------------------------------------")
print("| LET'S PLAY THE WORD GAUSSING GAME |")
print("-------------------------------------")
words=["apple","banana","cherry","mango","strowberry","pitch","cherry","coconut","graps"]

word=random.choice(words)

turns=10

print("gauss the characters of fruits :")
gausses=''   # start your gauss hear it is temparary storage area.

while(turns>0):
    is_faild=0
    for char in word:     # character of computer gaussed word
        if char in gausses:  # character check for coopurt character to player gaussed characters one by one
            print(char)
        else:
            print("_")
            is_faild+=1   # check that some characters are still missing so word is not complete
    if is_faild == 0:    
        print("you won the game...")
        print(f"your word is : {word}")
        print("----------")
        print("| FINISH |")
        print("----------") 
        print()
        break

    gauss=input("enter the character for fruit name:")
    gausses +=gauss   # tempary storage
    print(gausses)
    print()
    if gauss not in word:  # check that character is in word or not
        turns -=1
        print("you have lost the try , wrong word...")
        print()

        if turns==0:  # turns are finish so game over...
            print("you lost the game.........!!!!!!!!")
            print("----------")
            print("| FINISH |")
            print("----------")      
