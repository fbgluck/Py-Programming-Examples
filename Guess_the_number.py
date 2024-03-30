# This program is a guessing game. 
# Author: Fredric Gluck
# Date: 18 March 2024
# Version: 
# -----------------------------------
import random
# Explain the rules to the user
print(f"I will generate a random number between 1 and 10. You have 5 guesses to discover the number")
# Generate a random number between 1 and 100
target_number = random.randint(1,10)
# Set a variable to be equal to the number of guesses
guess_number = 1 # the number of the guess
# Set a variable to be the users name (input)
userName = input("What is your name? ")

while guess_number <= 5:
# Ask the user for a guess and assign it to a variable
    guess = int(input(f" OK, {userName}, What is your guess? "))
# Check to see if the random number is equal to the user's gues     
    print (f"Guess Number {guess_number}")
    if guess > target_number:
        print (f"You guessed {guess} and that's too high!")
    if guess < target_number:
        print (f"Your guess of {guess} is too low")
    if guess == target_number:
        print(f"You got it. The number was {target_number}")
        guess_number = 6 # set the loop so it stops
    guess_number = guess_number +1 #add one to the guess
    
# User has run out of guesses
print("Thanks for playing!")
    

    




