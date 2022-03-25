import random

top_range = input("Let's start.Give the highest number of your choice: ")
if(top_range.isdigit()):
    top_range=int(top_range)
    if(top_range<=0):
        print("Choose a range greater than zero")
else:
    print('Print a number next time')
    quit()

rand_number=random.randint(0,top_range)
guess=0
while top_range>0:
    guessed_number=input('Make your guess: ')
    guess+=1
    if(guessed_number.isdigit()):
        guessed_number=int(guessed_number)
    else:
        print("Print a number next time")
        continue

    if(guessed_number==rand_number):
        print('You got it right!')
        break
    elif(guessed_number<rand_number):
        print("Try a number greater")
    elif(guessed_number>rand_number):
        print("Try a number lesser")

print('You got it right in',guess,'guesses')


