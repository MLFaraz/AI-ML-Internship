def find_largest():
    print("=" * 35)
    print("   Largest Among Three Numbers")
    print("=" * 35)

    # Get user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    # Find the largest number
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    # Display the result
    print(f"\nThe largest number is: {largest}")


if __name__ == "__main__":
    find_largest()