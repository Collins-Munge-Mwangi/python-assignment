# A simple calculator program

# Get user input for the first number
num1_str = input("Enter the first number: ")
# Convert the string input to a floating-point number
num1 = float(num1_str)

# Get user input for the second number
num2_str = input("Enter the second number: ")
# Convert the string input to a floating-point number
num2 = float(num2_str)

# Get user input for the operation
operation = input("Enter an operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        # Handle the division by zero case
        result = "Error: Division by zero is not allowed."
else:
    # Handle an invalid operation input
    result = "Error: Invalid operation."

# Print the result
# Check if the result is a number or an error message
if isinstance(result, (int, float)):
    print(f"{num1} {operation} {num2} = {result}")
else:
    print(result)