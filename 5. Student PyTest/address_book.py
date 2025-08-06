class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Contact '{name}' added successfully!"

    def search_contact(self, name):
        if name in self.contacts:
            return f"Name: {name}, Phone: {self.contacts[name]}"
        else:
            return f"Contact '{name}' not found!"

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"Contact '{name}' deleted successfully!"
        else:
            return f"Contact '{name}' not found!"

    def list_contacts(self):
        output = ["Contacts:"]
        if not self.contacts:
            output.append("No contacts found")
        else:
            for name, phone in self.contacts.items():
                output.append(f"Name: {name}, Phone: {phone}")
        print('\n'.join(output))
        return '\n'.join(output)


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
            print(address_book.add_contact(name, phone))
        elif choice == '2':
            name = input("Enter name to search: ")
            print(address_book.search_contact(name))
        elif choice == '3':
            name = input("Enter name to delete: ")
            print(address_book.delete_contact(name))
        elif choice == '4':
            address_book.list_contacts()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
