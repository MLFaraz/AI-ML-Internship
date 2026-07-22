# Student Management System
# A complete mini project for managing student records
# Uses lists and dictionaries to store data temporarily (no database)

# Global list to hold all student records
# Each student is stored as a dictionary
all_students = []

def add_student():
    """Adds a new student to the system."""
    print("\n" + "=" * 40)
    print("         ADD NEW STUDENT")
    print("=" * 40)

    student_id = input("Enter Student ID: ").strip()

    # Make sure ID is unique
    for student in all_students:
        if student["id"] == student_id:
            print("A student with this ID already exists.")
            return

    name = input("Enter Student Name: ").strip()

    try:
        age = int(input("Enter Age: "))
        if age <= 0 or age > 120:
            print("Please enter a valid age.")
            return
    except ValueError:
        print("Age must be a number.")
        return

    course = input("Enter Course/Class: ").strip()

    try:
        marks = float(input("Enter Marks (out of 100): "))
        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return
    except ValueError:
        print("Marks must be a number.")
        return

    # Create student dictionary and add to list
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    all_students.append(student)
    print(f"\nStudent '{name}' has been added successfully!")


def view_all_students():
    """Displays all students in a neat table format."""
    print("\n" + "=" * 60)
    print("              ALL STUDENT RECORDS")
    print("=" * 60)

    if not all_students:
        print("No students found. The list is empty.")
        return

    # Print table header
    print(f"{'ID':<10} {'Name':<18} {'Age':<5} {'Course':<15} {'Marks':<6}")
    print("-" * 60)

    # Print each student
    for student in all_students:
        print(f"{student['id']:<10} {student['name']:<18} "
              f"{student['age']:<5} {student['course']:<15} {student['marks']:<6}")

    print("-" * 60)
    print(f"Total Students: {len(all_students)}")


def search_student():
    """Searches for a student by ID or Name."""
    print("\n" + "=" * 40)
    print("         SEARCH STUDENT")
    print("=" * 40)

    if not all_students:
        print("No students to search.")
        return

    print("Search by:")
    print("1. Student ID")
    print("2. Student Name")

    search_by = input("\nChoose option (1 or 2): ")

    found = False

    if search_by == "1":
        search_id = input("Enter Student ID: ").strip()
        for student in all_students:
            if student["id"] == search_id:
                display_student(student)
                found = True
                break

    elif search_by == "2":
        search_name = input("Enter Student Name: ").strip().lower()
        matches = [s for s in all_students if search_name in s["name"].lower()]

        if matches:
            print(f"\nFound {len(matches)} match(es):")
            for student in matches:
                display_student(student)
                print()
            found = True

    else:
        print("Invalid option.")
        return

    if not found:
        print("No student found matching your search.")


def display_student(student):
    """Helper function to display a single student's details."""
    print("\n  Student Details:")
    print(f"  ID     : {student['id']}")
    print(f"  Name   : {student['name']}")
    print(f"  Age    : {student['age']}")
    print(f"  Course : {student['course']}")
    print(f"  Marks  : {student['marks']}")


def update_student():
    """Updates information of an existing student."""
    print("\n" + "=" * 40)
    print("      UPDATE STUDENT INFORMATION")
    print("=" * 40)

    if not all_students:
        print("No students to update.")
        return

    student_id = input("Enter Student ID to update: ").strip()

    for student in all_students:
        if student["id"] == student_id:
            print(f"\nSelected Student: {student['name']}")
            print("Leave field blank to keep current value.\n")

            # Update name
            new_name = input(f"New Name [{student['name']}]: ").strip()
            if new_name:
                student["name"] = new_name

            # Update age
            new_age = input(f"New Age [{student['age']}]: ").strip()
            if new_age:
                try:
                    age = int(new_age)
                    if 0 < age <= 120:
                        student["age"] = age
                    else:
                        print("Invalid age. Keeping old value.")
                except ValueError:
                    print("Invalid input. Keeping old age.")

            # Update course
            new_course = input(f"New Course [{student['course']}]: ").strip()
            if new_course:
                student["course"] = new_course

            # Update marks
            new_marks = input(f"New Marks [{student['marks']}]: ").strip()
            if new_marks:
                try:
                    marks = float(new_marks)
                    if 0 <= marks <= 100:
                        student["marks"] = marks
                    else:
                        print("Marks out of range. Keeping old value.")
                except ValueError:
                    print("Invalid input. Keeping old marks.")

            print(f"\nStudent '{student['name']}' updated successfully!")
            return

    print("Student ID not found.")


def delete_student():
    """Deletes a student record from the system."""
    print("\n" + "=" * 40)
    print("       DELETE STUDENT RECORD")
    print("=" * 40)

    if not all_students:
        print("No students to delete.")
        return

    student_id = input("Enter Student ID to delete: ").strip()

    for i, student in enumerate(all_students):
        if student["id"] == student_id:
            print(f"\nStudent Found: {student['name']} (ID: {student['id']})")
            confirm = input("Are you sure you want to delete? (yes/no): ").strip().lower()

            if confirm == "yes":
                all_students.pop(i)
                print("Student record has been deleted.")
            else:
                print("Deletion cancelled.")
            return

    print("Student ID not found.")


def main():
    """Main function that runs the menu loop."""
    print("\n" + "=" * 50)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("  A simple system to manage student records")
    print("  using Python Lists and Dictionaries")
    print("=" * 50)

    while True:
        print("\n--- Main Menu ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Information")
        print("5. Delete Student Record")
        print("6. Exit Program")

        choice = input("\nEnter your choice (1-6): ").strip()

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
            print("\nThank you for using Student Management System!")
            print("All data is stored in memory and will be lost when you exit.")
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()
