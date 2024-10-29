# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of the exception
def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return #even after return then also fianlly executes

    except Exception as e:
        print(e)

    finally:
        print("i am inside finally") 

main()