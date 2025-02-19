amount=float(input("enter the amount : "))
print("here default currency is 💲")
curr=input("(rupees ₹ /pound 💷 /Euro 💶 /yuen 💴 )\n enter the currency you want to convert  : ")

if curr=="rupees":
    print(f"{amount} is {amount*86.828} in ₹")
elif curr=="pound":
    print(f"{amount} is {amount*0.79} in 💷")
elif curr=="Euro":
    print(f"{amount} is {amount*0.96} in 💶")
elif curr=="yean":
    print(f"{amount} is {amount*7.28} in 💴")
else:
    print(f"{curr} is wrong currency for this app")    
