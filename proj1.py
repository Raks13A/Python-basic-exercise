print('Welcome to the quiz game!')

interest=input('Hi! Interested to play? ')
if interest.lower()!='yes':
    quit()
else:
    print("OK.Let's play!")
score=0

answer = input('How many days does it take for the earth to orbit the Sun? ')
if answer=="365":
    print("Smart.You are right!")
    score += 1
else:
    print('Ohoo.Not right!')

answer = input('How many colors are there in the rainbow ')
if answer.lower()=="7" or 'seven':
    print("Smart.You are right!")
    score += 1
else:
    print('Ohoo.Not right!')

answer = input('RAM stands for ')
if answer.lower()=="random access memory":
    print("Smart.You are right!")
    score += 1
else:
    print('Ohoo.Not right!')

answer = input('What do you call a closed five sided polygon? ')
if answer.lower()=="pentagon":
    print("Smart.You are right!")
    score += 1
else:
    print('Ohoo.Not right!')

answer = input('What colour symbolises peace ')
if answer.lower()=="white":
    print("Smart.You are right!")
    score += 1
else:
    print('Ohoo.Not right!')

print("Great!You got "+str(score)+" score")