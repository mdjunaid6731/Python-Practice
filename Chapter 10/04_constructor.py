class Employee:
    language = "python"  # This is calss attribute
    salary = 1200000

    def __init__(self, name, salary, language):  #its a dunder method which is automatically called when object is created
        print("I am creating and object")
        self.name = name
        self.salary = salary
        self.language = language


    def getInfo(self):
        print(f"The language is {self.language}, The salary is {self.salary}")
    
    @staticmethod  #it is decorator in this fuct no need of self 
    def greet():
        print("Hello there")

rohan = Employee("Rohan", 1300000, "javascript")  # Object creation  init will be called here only
rohan.name = "Rohan"  # This is object/instance attribute
print(rohan.name, rohan.language, rohan.salary)
rohan.getInfo() 
#it is same as Employee.getInfo(rohan) the rohan object is passed so we need to add self parameter in calss function
rohan.greet()

