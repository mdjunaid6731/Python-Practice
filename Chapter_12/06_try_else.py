try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("i am inside else") #if try sucessfully runs the control come to else