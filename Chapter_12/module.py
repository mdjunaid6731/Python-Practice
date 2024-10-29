def myFunc():
    print("Helllo  World!")

print(__name__)  #Output: __main__
if __name__ == "__main__":
    #if this code is directly executed by running the file its present in
    print("We are directly runnning this code ")
    myFunc()
    