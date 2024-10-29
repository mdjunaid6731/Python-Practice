# The ‘enumerate’ function adds counter to an iterable and returns it

l = [3, 45, 56,535]

# index = 0
# for item in l:
#     print(f"The item number {index} is {item}")
#     index += 1
#This can be done usind enumerator

for index, item in enumerate(l):
     print(f"The item number {index} is {item}")
