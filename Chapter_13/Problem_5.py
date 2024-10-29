# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
a = [11,22,334,6,7,8,9]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, a))