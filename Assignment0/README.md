Basic Calculator Program
Description
This Python script provides a simple command-line calculator that allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division. It's designed to be user-friendly, guiding the user through input and handling common errors like division by zero. After each calculation, the user has the option to perform another calculation.

Features
Basic Operations: Supports addition (+), subtraction (-), multiplication (*), and division (/).

Number Input Validation: Ensures that users enter valid numerical inputs for calculations.

Operation Input Validation: Prompts the user to enter a valid mathematical operator.

Division by Zero Handling: Prevents errors by detecting and reporting attempts to divide by zero.

Repeat Calculations: Allows the user to perform multiple calculations in a single session without restarting the program.

How to Run
Save the file: Save the provided Python code as a .py file (e.g., calculator.py).

Open a terminal or command prompt: Navigate to the directory where you saved the file.

Execute the script: Run the script using the Python interpreter:

python calculator.py

Usage
Once the program starts, it will prompt you to:

Enter the first number.

Enter the second number.

Enter the desired operation (+, -, *, or /).

The program will then display the result of the calculation. After the result is shown, it will ask if you want to perform "another calculation." You can type yes (or y) to continue or no (or n) to exit the program.

Example Session
--- Welcome to the Basic Calculator! ---
Let's do some math!

Enter the first number: 10
Enter the second number: 5
Enter the operation (+, -, *, /): +

Result: 10.0 + 5.0 = 15.0

--- Calculation complete! ---
Do you want to perform another calculation? (yes/no): yes
--- Welcome to the Basic Calculator! ---
Let's do some math!

Enter the first number: 20
Enter the second number: 0
Enter the operation (+, -, *, /): /
Error: Cannot divide by zero!

Result: Error: Division by zero

--- Calculation complete! ---
Do you want to perform another calculation? (yes/no): no
Thanks for using the calculator! Goodbye! 👋
