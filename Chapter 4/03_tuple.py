# A tuple is an immutable data type in python.
a = () #Empty tuple
b = (2,) #one element tuple
c = (2,3,7,6,"apple","john") #multiple item tuple

print(type(c))  #tuple retunrs new tuple when a new operation performed on them

# Tuples methods
t1 = (3,8,87,90,23,67,3,12,11,7)
print(t1)

# Returns the number of occurrences of a specified value in the tuple
print("Count: ", t1.count(3))

# Returns the index of the first occurrence of a specified value in the tuple.
print("Index: ", t1.index(90))

# You can concatenate two tuples.
tuple1 = (1,2)
tuple2 = (3,4)
print("Concatination:",tuple1 + tuple2)

# You can find the length of a tuple using len().
print("Length:", len(t1))

#slicing
print("Slicing:",t1[2:6])

# Get the minimum and maximum values in a tuple 
print("Minimum: ", min(t1))
print("Maximum: ",max(t1))


