# f = open("file.txt") 
# f.read()
# f.close()

# Same can be done using with statement:
with open("file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file
