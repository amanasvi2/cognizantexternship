# Project 2: Number Guessing Game
import random
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10
print("Welcome to the Number Guessing Game!")

while attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break
else:
    print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")