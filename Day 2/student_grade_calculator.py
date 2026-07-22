# Student Grade Calculator
# Calculates grade based on marks entered by the user

def get_grade(marks):
    """Returns grade letter based on marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def main():
    print("=" * 40)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 40)

    name = input("Enter student name: ")

    # Get marks for 5 subjects
    subjects = ["Math", "Science", "English", "History", "Computer"]
    total = 0

    for subject in subjects:
        while True:
            try:
                marks = float(input(f"Enter marks for {subject} (out of 100): "))
                if 0 <= marks <= 100:
                    total += marks
                    break
                else:
                    print("Marks should be between 0 and 100. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    average = total / len(subjects)
    grade = get_grade(average)

    print("\n" + "-" * 40)
    print(f"Student Name: {name}")
    print(f"Total Marks: {total} / {len(subjects) * 100}")
    print(f"Average: {average:.2f}%")
    print(f"Grade: {grade}")
    print("-" * 40)

    if grade == "F":
        print("Status: Failed")
    else:
        print("Status: Passed")

if __name__ == "__main__":
    main()
