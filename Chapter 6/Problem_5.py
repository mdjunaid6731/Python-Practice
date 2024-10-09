# Write a program which finds out whether a given name is present in a list or not.

l = ["John" , "Rohan", "Atif", "Divya"]

name = input("Enter your name: ")

if(name in l):
    print("your name is in the list")
else:
    print("Your name is not in the list")