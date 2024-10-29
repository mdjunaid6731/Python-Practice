a = int(input("Enter number"))
b = int(input("Enter number"))

if(b == 0):
    raise ZeroDivisionError("Hey our program is nor meant to divide number by zero")
else:
    print(f"The division a/b is {a/b}")