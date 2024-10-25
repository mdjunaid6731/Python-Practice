class Employee:    
    company = "ITC"
    name = "Rohan"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company} ")

class Coder:
    language ="Python"
    def printLanguage(self):
        print(f"Out of all languages here is your language : {self.language}")
        
class Programmer(Employee, Coder):  
    company = "ITC Innfotech"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good in {self.language} language")


b = Programmer()

b.show()   
b.printLanguage()       
b.showlanguage()
