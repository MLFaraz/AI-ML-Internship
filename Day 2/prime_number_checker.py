# Prime Number Checker
# Checks if a number is prime and lists primes in a range

def is_prime(n):
    """Returns True if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    print("=" * 40)
    print("      PRIME NUMBER CHECKER")
    print("=" * 40)

    while True:
        print("\n1. Check if a number is prime")
        print("2. List prime numbers in a range")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ")

        if choice == "1":
            try:
                num = int(input("Enter a number: "))
                if is_prime(num):
                    print(f"{num} is a prime number.")
                else:
                    print(f"{num} is not a prime number.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            try:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))

                primes = [n for n in range(start, end + 1) if is_prime(n)]
                print(f"\nPrime numbers between {start} and {end}:")
                print(primes)
                print(f"Total: {len(primes)} prime numbers found.")
            except ValueError:
                print("Please enter valid integers.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
