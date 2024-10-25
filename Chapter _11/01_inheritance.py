class Employee:    #Parent / Base class
    company = "ITC"
    name = "Rohan"
    salary =233333
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} ")


# class Programmer:
#     company = "ITC Innfotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary} ")

#     def showlanguage(self):
#         print(f"The name is {self.name} and he is good in {self.language} language")

        
class Programmer(Employee):  # Child / Dirived class
    company = "ITC Innfotech"
    name = "Rohan"
    language = "Python"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")


b = Programmer()
print(b.company)
b.show()         #This is  inherited method from parent class so it can called by Programmer class object 
b.showlanguage()
