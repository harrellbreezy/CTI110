# Briana Harrell
# Decemeber 6 2025
# LLM_LAB1
# this program allows the user to perform basic arithmetic operations

def calculator():
    print("Basic Arithmetic Calculator")
    print("---------------------------")

    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user for an operation
    print("Choose an operation: +, -, *, /")
    operation = input("Enter the operation: ")

    # Perform the calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operation entered.")
        return

    # Display the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

    # Ask if the user wants another calculation
    again = input("Would you like to do another calculation? (yes/no): ")

    if again not in ("yes", "y"):
            print("Goodbye!")
            

# Run the calculator
calculator()
