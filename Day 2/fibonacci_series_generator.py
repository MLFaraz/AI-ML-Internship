# Fibonacci Series Generator
# Generates Fibonacci sequence up to a given number of terms

def fibonacci_series(n):
    """Returns a list of first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    series = [0, 1]
    for i in range(2, n):
        next_num = series[-1] + series[-2]
        series.append(next_num)
    return series

def main():
    print("=" * 40)
    print("   FIBONACCI SERIES GENERATOR")
    print("=" * 40)
    print("The Fibonacci series starts with 0 and 1,\n"
          "and each next number is the sum of the previous two.\n")

    try:
        terms = int(input("How many terms do you want? "))

        if terms <= 0:
            print("Please enter a positive number.")
            return

        result = fibonacci_series(terms)

        print(f"\nFirst {terms} terms of Fibonacci series:")
        print(" -> ".join(str(num) for num in result))

        # Show some extra info
        if len(result) > 1:
            print(f"\nLast number: {result[-1]}")
            print(f"Sum of all terms: {sum(result)}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
