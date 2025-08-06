class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Contact '{name}' added successfully!")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}, Phone: {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found!")

    def list_contacts(self):
        print("Contacts:")
        for name, phone in self.contacts.items():
            print(f"Name: {name}, Phone: {phone}")


def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address_book.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to search: ")
            address_book.search_contact(name)
        elif choice == '3':
            name = input("Enter name to delete: ")
            address_book.delete_contact(name)
        elif choice == '4':
            address_book.list_contacts()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
