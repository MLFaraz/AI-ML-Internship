# Multiplication Table Generator
# Generates multiplication table for any number up to a specified range

def generate_table():
    print("=" * 40)
    print("   MULTIPLICATION TABLE GENERATOR")
    print("=" * 40)

    try:
        number = int(input("Enter the number for the table: "))
        limit = int(input("Enter how many multiples you want (e.g., 10): "))

        if limit <= 0:
            print("Limit must be greater than zero.")
            return

        print(f"\nMultiplication Table of {number}:")
        print("-" * 25)

        for i in range(1, limit + 1):
            result = number * i
            print(f"  {number} x {i:2} = {result}")

        print("-" * 25)

    except ValueError:
        print("Please enter valid numbers only.")

if __name__ == "__main__":
    generate_table()
