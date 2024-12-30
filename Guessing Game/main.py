# Program will generate a value and then the user will need
# to guess the value

import random


value = random.randint(1,100) # from 1 till 100
count = 0
while True:
    user_guess = int(input("Enter your guess "))
    count += 1
    if user_guess == value:
        print("You won ",count)
        break
    elif user_guess < value:
        print("Guess higher value")
    else:
        print("Guess higher lower value")