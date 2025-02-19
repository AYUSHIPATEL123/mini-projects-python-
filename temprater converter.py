import math

temp=float(input("enter the temprater : "))
unit=input("enter the unit (C/F): ")

if unit=="C":
    result=(temp*9)/5 + 32;
    print(f"tempratet is 👉️ {round(result,1)}°F");
elif unit=="F":
    result=(temp-32)*5/9;
    print(f"tempratet is 👉️ {round(result,1)}°C");
else:
    print(f"your {unit} is wrong.");

