# Student Record Management System
# Uses lists and dictionaries to manage student records temporarily

students = []  # List to store all student dictionaries

def add_student():
    """Adds a new student record."""
    print("\n--- Add New Student ---")

    roll = input("Enter Roll Number: ")

    # Check if roll number already exists
    for s in students:
        if s["roll"] == roll:
            print("A student with this roll number already exists.")
            return

    name = input("Enter Name: ")

    try:
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Invalid input for age or marks.")
        return

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print(f"Student '{name}' added successfully.")

def view_all_students():
    """Displays all student records."""
    print("\n--- All Student Records ---")

    if not students:
        print("No students found.")
        return

    print(f"{'Roll':<10} {'Name':<20} {'Age':<5} {'Marks':<6}")
    print("-" * 45)

    for s in students:
        print(f"{s['roll']:<10} {s['name']:<20} {s['age']:<5} {s['marks']:<6}")

def search_student():
    """Searches for a student by roll number."""
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ")

    for s in students:
        if s["roll"] == roll:
            print(f"\nStudent Found:")
            print(f"  Roll: {s['roll']}")
            print(f"  Name: {s['name']}")
            print(f"  Age: {s['age']}")
            print(f"  Marks: {s['marks']}")
            return

    print("Student not found.")

def update_student():
    """Updates an existing student record."""
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number to update: ")

    for s in students:
        if s["roll"] == roll:
            print(f"Current Name: {s['name']}")
            new_name = input("Enter new name (press Enter to keep same): ")
            if new_name:
                s["name"] = new_name

            try:
                new_age = input("Enter new age (press Enter to keep same): ")
                if new_age:
                    s["age"] = int(new_age)

                new_marks = input("Enter new marks (press Enter to keep same): ")
                if new_marks:
                    s["marks"] = float(new_marks)
            except ValueError:
                print("Invalid input. Update cancelled.")
                return

            print("Student record updated.")
            return

    print("Student not found.")

def delete_student():
    """Deletes a student record."""
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ")

    for i, s in enumerate(students):
        if s["roll"] == roll:
            confirm = input(f"Are you sure you want to delete '{s['name']}'? (yes/no): ")
            if confirm.lower() == "yes":
                students.pop(i)
                print("Student record deleted.")
            else:
                print("Deletion cancelled.")
            return

    print("Student not found.")

def main():
    print("=" * 40)
    print("  STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 40)

    while True:
        print("\n1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("\nThank you! Exiting...")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
