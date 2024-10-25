class Employee:
    def __init__(self):
        print("Constructot of Employee")
    a =1

class Programmer(Employee):
    def __init__(self):
        print("Constructot of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()    # Parent methods will also run
        print("Constructot of Manager")
    c = 3

# o = Employee()
# print(o.a) # prints the  a attr

# o = Programmer()
# print(o.a , o.b)

o = Manager()
print(o.a, o.b, o.c)

