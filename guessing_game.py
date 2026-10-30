
import random


# ==========================================
# GUESSING NUMBER GAME
# Created by: Ivan Firmansyah
# Description: Guess a random number from 0 to 10
# ==========================================


# Function 1: Generate a random number
def generate_number():
    number = random.randint(0, 10)
    return number


# Function 2: Get the player's guess
def get_guess():
    while True:
        try:
            guess = int(input("Guess a number (0-10): "))

            # Check if the guess is within the range
            if 0 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 0 and 10.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function 3: Check the player's guess
def check_guess(guess, number):

    if guess == number:
        print("Yeah, you guessed it!")
        return True

    elif guess < number:
        print("Too low, try again!")
        return False

    else:
        print("Too high, try again!")
        return False


# Function 4: Main guessing game
def guessing_game():

    while True:

        print("\n================================")
        print("       GUESSING NUMBER GAME")
        print("================================")

        # Computer generates a random number
        number = generate_number()

        print("I have selected a number between 0 and 10.")

        # Keep asking until the player guesses correctly
        while True:

            guess = get_guess()

            correct = check_guess(guess, number)

            if correct:
                break

        # Ask the player to play again
        again = input("\nDo you want to play again? (yes/no): ")

        if again.lower() not in ["yes", "y"]:
            print("\nThank you for playing! Goodbye!")
            break


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():
    guessing_game()


# Start the program
if __name__ == "__main__":
    main()
