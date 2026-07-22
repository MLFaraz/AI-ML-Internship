def even_odd_checker():
    print("=" * 30)
    print("   Even or Odd Checker")
    print("=" * 30)

    # Get user input
    number = int(input("Enter an integer: "))

    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"\n{number} is an Even number.")
    else:
        print(f"\n{number} is an Odd number.")


if __name__ == "__main__":
    even_odd_checker()