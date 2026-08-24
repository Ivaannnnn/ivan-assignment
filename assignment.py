import random


# =========================
# CALCULATOR FUNCTION
# =========================
def calculator():
    while True:
        num1 = float(input("\nEnter the first number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            result = num1 / num2
        else:
            print("Invalid operation.")
            continue

        print(f"Result: {num1} {operation} {num2} = {result}")

        again = input("Do you want to calculate again? (yes/no): ")

        if again.lower() != "yes":
            break


# =========================
# GUESSING GAME FUNCTION
# =========================
def guessing_game():
    while True:
        secret_number = random.randint(1, 10)

        guess = int(input("\nGuess a number between 1 and 10: "))

        if guess == secret_number:
            print("Yeah, you guessed it!")
        else:
            print("Try again")

        again = input("Do you want to play again? (yes/no): ")

        if again.lower() != "yes":
            break


# =========================
# MAIN MENU FUNCTION
# =========================
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