# GUESS THE NUMBER GAME
# The computer randomly chooses a number, and the user has to guess it.

import random  # Import random module to generate random numbers

number_to_guess = random.randint(1, 10)  # Random number between 1 and 10
attempts = 0

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 10.")

# Loop until the user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        break