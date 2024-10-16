# Python has an open() function for opening files. It takes 2 parameters: filename and mode.


f = open("file.txt", "r")  #by default its a read mode
data = f.read()
print(data)
f.close() 