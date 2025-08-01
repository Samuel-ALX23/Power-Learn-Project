# This script creates a basic calculator that performs addition, subtraction,
# multiplication, or division based on user input.

def basic_calculator():
    """
    Asks the user for two numbers and a mathematical operation,
    then performs the calculation and prints the result.
    Allows the user to perform multiple calculations.
    """
    while True: # Outer loop to allow playing again
        print("--- Welcome to the Basic Calculator! ---")
        print("Let's do some math!\n")

        # Get the first number from the user
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                break # Exit loop if input is a valid number
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Get the second number from the user
        while True:
            try:
                num2 = float(input("Enter the second number: "))
                break # Exit loop if input is a valid number
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Get the operation from the user
        while True:
            operation = input("Enter the operation (+, -, *, /): ")
            if operation in ['+', '-', '*', '/']:
                break # Exit loop if input is a valid operation
            else:
                print("Invalid operation. Please enter +, -, *, or /.")

        result = None # Initialize result variable

        # Perform the calculation based on the chosen operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0: # Check for division by zero
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero!")
                # No return here, so the "play again" prompt can still appear
                result = "Error: Division by zero" # Set result to error message
        else:
            # This case should ideally not be reached due to the input validation loop
            print("An unexpected error occurred with the operation.")


        # Print the result
        if result is not None and not isinstance(result, str): # Check if result is not an error string
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        elif isinstance(result, str): # If result is an error message
            print(f"\nResult: {result}")
        print("\n--- Calculation complete! ---")

        # Offer to play again
        while True:
            play_again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if play_again in ["yes", "y"]:
                break # Break from this inner loop to restart the outer calculator loop
            elif play_again in ["no", "n"]:
                print("Thanks for using the calculator! Goodbye! 👋")
                return # Exit the basic_calculator function entirely
            else:
                print("Please enter 'yes' or 'no'.")

# Run the calculator when the script is executed
if __name__ == "__main__":
    basic_calculator()
