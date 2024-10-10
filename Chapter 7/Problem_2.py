# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Junaid", "Soham", "Sachin", "Rahul"]

l = ["Junaid", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Good Morning {name}")