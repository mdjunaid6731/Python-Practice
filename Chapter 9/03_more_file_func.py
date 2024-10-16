# f = open("file.txt")

# lines = f.readlines()  #returs lines of list

# print(lines, type(lines))

# f.close()

f = open("file.txt")

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4 == "", type(line3)) #return empty string true

f.close()
