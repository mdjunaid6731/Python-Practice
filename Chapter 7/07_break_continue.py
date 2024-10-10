# ‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now.

for i in range(100):
    if(i == 24):
        break #Exit the loop
    print(i)

# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.
for i in range(100):
    if(i == 24):
        continue #Skip  this iteration
    print(i)
