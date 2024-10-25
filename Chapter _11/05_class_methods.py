# A class method is a method which is bound to the class and not the object of the class.

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The  class attribute of a is {cls.a}")


e = Employee()
e.a = 45 #To prevent instance object very use class method if  we run this  line output will 1 because of calss methos decorator

e.show()