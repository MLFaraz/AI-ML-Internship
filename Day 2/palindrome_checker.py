# Palindrome Checker
# Checks if a word, phrase, or number reads the same forwards and backwards

def clean_text(text):
    """Removes spaces and converts to lowercase for comparison."""
    return "".join(char.lower() for char in text if char.isalnum())

def is_palindrome(text):
    """Checks if the cleaned text is a palindrome."""
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]

def main():
    print("=" * 40)
    print("      PALINDROME CHECKER")
    print("=" * 40)
    print("Checks if a word, phrase, or number is a palindrome.\n")

    while True:
        user_input = input("Enter text to check (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            print("Thanks for using the Palindrome Checker!")
            break

        cleaned = clean_text(user_input)

        if len(cleaned) == 0:
            print("Please enter something meaningful.\n")
            continue

        if is_palindrome(user_input):
            print(f"Yes! '{user_input}' is a palindrome.\n")
        else:
            print(f"No, '{user_input}' is not a palindrome.")
            print(f"Reversed: {cleaned[::-1]}\n")

if __name__ == "__main__":
    main()
