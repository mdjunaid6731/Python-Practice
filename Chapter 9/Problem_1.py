# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twikel is present")
else:
    print("The word twikel is not present")
f.close()