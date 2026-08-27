import random


# ====================
# CALCULATOR FUNCTIONS
# ====================
# Function to get a number from the user
def get_number(message):
    number = float(input(message))
    return number

# Function to get the operation
def get_operation():
    operation = input("Choose an operation (+, -, *, /): ")
    return operation

# Function to calculate the result
def calculate(num1, num2, operation):

    if operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1 - num2

    elif operation == "*":
        return num1 * num2

    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."

    else:
        return "Invalid operation."

# Main calculator function
def calculator():

    while True:

        print("\n===== CALCULATOR =====")

        # Get first number
        num1 = get_number("Enter the first number: ")

        # Get operation
        operation = get_operation()

        # Get second number
        num2 = get_number("Enter the second number: ")

        # Calculate result
        result = calculate(num1, num2, operation)

        # Display result
        print(f"Result: {num1} {operation} {num2} = {result}")

        # Ask user to calculate again
        again = input("Do you want to calculate again? (yes/no): ")

        if again.lower() != "yes":
            break


# ========================
# GUESSING GAME FUNCTIONS
# ========================

# Function to generate a random number
def generate_number():
    return random.randint(1, 10)

# Function to get the player's guess
def get_guess():
    guess = int(input("Guess a number between 1 and 10: "))
    return guess

# Function to check the guess
def check_guess(guess, secret_number):

    if guess == secret_number:
        print("Yeah, you guessed it!")
    else:
        print("Try again")

# Main guessing game function
def guessing_game():

    while True:

        print("\n===== GUESSING GAME =====")

        # Generate random number
        secret_number = generate_number()

        # Get player's guess
        guess = get_guess()

        # Check the guess
        check_guess(guess, secret_number)

        # Ask player to play again
        again = input("Do you want to play again? (yes/no): ")

        if again.lower() != "yes":
            break


# ===================
# MAIN MENU FUNCTION
# ===================

def main():

    while True:

        print("\n===== MAIN MENU =====")
        print("1. Calculator")
        print("2. Guessing Number Game")
        print("3. Quit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            guessing_game()

        elif choice == "3":
            print("Thank you! Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()