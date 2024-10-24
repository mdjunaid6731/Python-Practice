# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft" 
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Rohan", 1200000, 245098)
print(p.name)
print(p.salary)
print(p.pin)