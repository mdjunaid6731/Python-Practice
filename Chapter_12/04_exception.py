try:
    a = int(input("Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyy")
    print(v)

# except Exception as e:
#     print(e)

print("Thank You")   #prgrom will not get terminate ,  it will give error messaeg and excute next line