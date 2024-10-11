'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 1 x 2
factorial(3) = 1 X 2 X 3
factorial(4) = 1 X 2 X 3 X 4
factorial(5) = 1 X 2 X 3 X 4 X 5
factorial(n) = n X n-1 X ........X 3 X 2 X 1

factorial(n) n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):   # base caondition to avoid infinte calls
        return 1
    return n * factorial(n-1)


n =  int(input("Enter the nuumber: "))
print(f"The factorial of {n} is {factorial(n)}")
