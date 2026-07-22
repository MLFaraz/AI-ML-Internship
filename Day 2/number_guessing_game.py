# Number Guessing Game
# The computer picks a random number, and the user tries to guess it

import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=" * 40)
    print("      NUMBER GUESSING GAME")
    print("=" * 40)
    print("I have picked a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            if guess == secret_number:
                print(f"\nCongratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts left.\n")

        except ValueError:
            print("Please enter a valid number.\n")

    print(f"\nGame Over! The secret number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
