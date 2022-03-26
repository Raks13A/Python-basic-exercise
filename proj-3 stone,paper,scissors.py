import random

user_wins=0
computer_wins=0

options=["stone","paper","scissor"]
times=0
while times<5:
    user_input=input("Type stone/paper/scissor or q to quit: ").lower()
    if user_input=="q":
        break
    elif user_input not in options:
        continue
    random_input=random.randint(0,2)
    computer_input=options[random_input]
    print("Computer picked: ",computer_input)

    if user_input=="scissor" and computer_input=="paper":
        print("You won!")
        user_wins+=1
    elif user_input=="paper" and computer_input=="stone":
        print("You won!")
        user_wins += 1
    elif user_input=="stone" and computer_input=="scissor":
        print("You won!")
        user_wins += 1
    else:
        print("you lost!")
        computer_wins+=1

    print("You won "+ str(user_wins)+" times.")
    print("You won "+ str(computer_wins)+" times.")
    times+=1
print("Goodbye!")

