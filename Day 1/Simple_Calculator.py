def calculator():
    print("=" * 30)
    print("   Simple Calculator")
    print("=" * 30)

    # Get user input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operator.")
        return

    # Display result
    print(f"\nResult: {num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    calculator()