# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 4

o = Demo()
print(o.a) #print the class attr because instance attr is not present
o.a = 0  #instance attr is set
print(o.a)  #prints the instance attr because instance attr is present
print(Demo.a) #print the class attr

# it does not change the class attribute