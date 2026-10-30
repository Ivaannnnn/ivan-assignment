"""
Chapter 6: Design with Functions - Integrated Demonstration
Book: Fundamentals of Python: First Programs (2nd Edition)

This script combines top-down design, helper functions, recursion,
and higher-order functions into one executable Python program.
"""

from functools import reduce


# ==========================================================
# 1. TOP-DOWN DESIGN & HELPER FUNCTIONS
# ==========================================================

# Function: format_header
# What it is: A helper function with default/optional parameters.
# What it does: Creates a formatted visual banner for output displays.
def format_header(title, border_char="="):
    border = border_char * len(title)
    return f"\n{border}\n{title}\n{border}"


# ==========================================================
# 2. RECURSIVE FUNCTIONS
# ==========================================================

# Function: recursive_factorial
# What it is: A recursive function calculating n!
# What it does: Multiplies n by recursive calls of (n - 1) until reaching n <= 1.
def recursive_factorial(n):
    if n <= 1:
        return 1  # Base Case: stops infinite recursion
    return n * recursive_factorial(n - 1)  # Recursive Step


# Function: recursive_sum
# What it is: A recursive function calculating list totals.
# What it does: Adds the head of the list to the recursive sum of the tail.
def recursive_sum(numbers):
    if not numbers:
        return 0  # Base Case: empty list returns 0
    return numbers[0] + recursive_sum(numbers[1:])  # Recursive Step


# ==========================================================
# 3. HIGHER-ORDER FUNCTIONS & LAMBDAS
# ==========================================================

# Function: demonstrate_higher_order_functions
# What it is: A demonstration function utilizing first-class functions.
# What it does: Applies map(), filter(), and reduce() with lambda functions.
def demonstrate_higher_order_functions(data):
    print(format_header("HIGHER-ORDER FUNCTIONS & LAMBDAS", "-"))
    print(f"Original Input List: {data}")

    # map(): Applies a lambda function to double every value in the list
    doubled = list(map(lambda x: x * 2, data))
    print(f"Mapped List (Doubled values): {doubled}")

    # filter(): Keeps only items that pass the lambda condition (even numbers)
    evens = list(filter(lambda x: x % 2 == 0, data))
    print(f"Filtered List (Even numbers only): {evens}")

    # reduce(): Aggregates all numbers in the list into a single accumulated sum
    total_sum = reduce(lambda x, y: x + y, data, 0)
    print(f"Reduced Value (Sum of all items): {total_sum}")


# ==========================================================
# 4. MAIN PROGRAM CONTROL (TOP-LEVEL MANAGER)
# ==========================================================

# Function: main
# What it is: The entry-point manager function coordinating top-down execution.
# What it does: Sets up test data and calls each subsystem step-by-step.
def main():
    print(format_header("CHAPTER 6 INTEGRATED DEMO PROGRAM"))

    # Test dataset definition
    numbers_dataset = [1, 2, 3, 4, 5, 6]

    # Subsystem 1: Run Recursion Tests
    print(format_header("RECURSION DEMO", "-"))
    factorial_input = 5
    print(f"Factorial of {factorial_input}! = {recursive_factorial(factorial_input)}")
    print(f"Recursive Sum of {numbers_dataset} = {recursive_sum(numbers_dataset)}")

    # Subsystem 2: Run Higher-Order Function Tests
    demonstrate_higher_order_functions(numbers_dataset)


# Standard Python Guard: Ensures code runs when executed directly
if __name__ == "__main__":
    main()