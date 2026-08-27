import random


# =====================
# CALCULATOR FUNCTIONS
# =====================
# Function to get a number from the user
def get_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Main calculator function
def calculator():
    while True:
        print("\n--- Calculator ---")

        num1 = get_number()
        operation = input("Choose (+, -, *, /): ")
        num2 = get_number()

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operation."

        print("Result:", result)

        again = input("Do you want to calculate again? (yes/no): ")

        if again.lower() != "yes":
            break

# ==============
# GUESSING GAME
# ==============
# Function to generate a random number
def generate_number():
    return random.randint(1, 10)

# Function to get the player's guess
def get_guess():
    while True:
        try:
            guess = int(input("Guess a number (1-10): "))

            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number from 1 to 10.")

        except ValueError:
            print("Please enter a valid number.")

# Function to check the guess
def check_guess(guess, number):
    if guess == number:
        print("Yeah, you guessed it!")
    else:
        print("Try again")

# Main guessing game function
def guessing_game():
    while True:
        print("\n--- Guessing Game ---")

        number = generate_number()
        guess = get_guess()

        check_guess(guess, number)

        again = input("Do you want to play again? (yes/no): ")

        if again.lower() != "yes":
            break

# =============
# MAIN PROGRAM
# =============

def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Calculator")
        print("2. Guessing Game")
        print("3. Quit")

        choice = input("Choose: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            guessing_game()
        elif choice == "3":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice.")

# Start the program
main()