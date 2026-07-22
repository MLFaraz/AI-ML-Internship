# Password Strength Checker
# Evaluates password strength based on basic conditions

def check_strength(password):
    """Checks password strength and returns a score and message."""
    score = 0
    feedback = []

    # Condition 1: Minimum length of 8 characters
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Condition 2: Contains uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Condition 3: Contains lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Condition 4: Contains digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Condition 5: Contains special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")

    return score, feedback

def main():
    print("=" * 40)
    print("    PASSWORD STRENGTH CHECKER")
    print("=" * 40)
    print("A strong password should have:
"
          "  - At least 8 characters
"
          "  - Uppercase and lowercase letters
"
          "  - At least one number
"
          "  - At least one special character
")

    password = input("Enter a password to check: ")

    score, feedback = check_strength(password)

    # Determine strength label
    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    elif score >= 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    print(f"\nPassword: {'*' * len(password)}")
    print(f"Length: {len(password)} characters")
    print(f"Strength: {strength} ({score}/5)")

    if feedback:
        print("\nSuggestions to improve:")
        for tip in feedback:
            print(f"  - {tip}")
    else:
        print("\nGreat job! Your password meets all requirements.")

if __name__ == "__main__":
    main()
