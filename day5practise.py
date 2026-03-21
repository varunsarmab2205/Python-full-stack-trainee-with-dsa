#Smart Number Guessing Game

import random

print(" Welcome to the Number Guessing Game!\n")

# Computer chooses number
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 5

print("I have chosen a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

# Loop starts
while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Conditions
    if guess == secret_number:
        print(f" Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print(" Too low! Try a higher number.")
    else:
        print(" Too high! Try a lower number.")

    print(f"Attempts left: {max_attempts - attempts}\n")

# After loop ends
if guess != secret_number:
    print(f" Game Over! The correct number was {secret_number}")

print("\nThanks for playing! ")
