st = "Hey Rohan you are amazing"

f = open("myfile.txt", "w") #write mode
f.write(st)
f.close()

# r – open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# ‘rb’ will open for read in binary mode.
# ‘rt’ will open for read in text mode.
