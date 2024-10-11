# Snake , Water, Gun Game
# 1 for snake
# -1 for water
# 0 for gun

import random

computer = random.choice([-1, 0, 1])
userstr = input("Enter your choice (s,w,g): ")
userDict = {"s":1, "w":-1, "g":0 }
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

user = userDict[userstr]

# Bu now we have two numbers(variables), user and computer
print(f"You Choose {reverseDict[user]}\nComputer Choose {reverseDict[computer]}")

if(computer == user):
    print("Its a draw")

else:

    if(computer == -1 and user == 1):
        print("You Win!")

    elif(computer == -1 and user == 0):
        print("You Lose!")

    elif(computer == 1 and user == -1):
        print("You Lose!")

    elif(computer == 1 and user == 0):
        print("You Win!")

    elif(computer == 0 and user == -1):
        print("You Win!")

    elif(computer == 0 and user == 1):
        print("You Lose!")

    else:
        print("Something Went worng")

