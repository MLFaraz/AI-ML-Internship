# Mini Contact Book
# A simple contact management system using dictionaries

contacts = {}  # Dictionary to store contacts: name -> phone number

def add_contact():
    """Adds a new contact to the book."""
    print("\n--- Add Contact ---")
    name = input("Enter contact name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if name in contacts:
        print(f"'{name}' already exists. Use update to change the number.")
        return

    phone = input("Enter phone number: ").strip()

    if not phone:
        print("Phone number cannot be empty.")
        return

    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")

def search_contact():
    """Searches for a contact by name."""
    print("\n--- Search Contact ---")
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print(f"\nName: {name}")
        print(f"Phone: {contacts[name]}")
    else:
        print(f"No contact found with the name '{name}'.")

def update_contact():
    """Updates an existing contact's phone number."""
    print("\n--- Update Contact ---")
    name = input("Enter name to update: ").strip()

    if name not in contacts:
        print(f"No contact found with the name '{name}'.")
        return

    print(f"Current phone: {contacts[name]}")
    new_phone = input("Enter new phone number: ").strip()

    if new_phone:
        contacts[name] = new_phone
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Update cancelled. Phone number cannot be empty.")

def delete_contact():
    """Deletes a contact from the book."""
    print("\n--- Delete Contact ---")
    name = input("Enter name to delete: ").strip()

    if name not in contacts:
        print(f"No contact found with the name '{name}'.")
        return

    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ")
    if confirm.lower() == "yes":
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Deletion cancelled.")

def view_all_contacts():
    """Displays all contacts."""
    print("\n--- All Contacts ---")

    if not contacts:
        print("Contact book is empty.")
        return

    print(f"{'Name':<25} {'Phone Number'}")
    print("-" * 45)

    for name, phone in sorted(contacts.items()):
        print(f"{name:<25} {phone}")

def main():
    print("=" * 40)
    print("       MINI CONTACT BOOK")
    print("=" * 40)

    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            view_all_contacts()
        elif choice == "6":
            print("\nGoodbye! Your contacts were not saved to a file.")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
