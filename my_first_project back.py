import random

guess = input("Guess a number Between 1 and 10 if you would be so kind\n")
guess = int(guess)

number = random.randint(1,10)

if(guess == number):
    print("YOU HAVE GUESSED THE RIGHT NUMBER CONGRATS")
else:
    print("You have guessed the wrong number.\n You fucking suck at this")
