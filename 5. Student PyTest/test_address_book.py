# Import the pytest library
import pytest
# Import the AddressBook class from the address_book module
from address_book import AddressBook

# Define a pytest fixture to create an instance of AddressBook before each test function
@pytest.fixture
def address_book():
    return AddressBook()

# Test case to check if a contact can be added successfully
def test_add_contact(address_book):
    # Add a contact to the address book
    address_book.add_contact("John Doe", "1234567890")
    # Assert that the contact has been added to the address book
    assert address_book.contacts["John Doe"] == "1234567890"

# Test case to check if an existing contact can be searched for
def test_search_existing_contact(address_book):
    # Add a contact to the address book
    address_book.add_contact("John Doe", "1234567890")
    # Search for the existing contact
    assert address_book.search_contact("John Doe") == "Name: John Doe, Phone: 1234567890"

# Test case to check if a non-existent contact returns an appropriate message when searched for
def test_search_nonexistent_contact(address_book):
    # Search for a non-existent contact
    assert address_book.search_contact("Nonexistent") == "Contact 'Nonexistent' not found!"

# Test case to check if an existing contact can be deleted
def test_delete_existing_contact(address_book):
    # Add a contact to the address book
    address_book.add_contact("John Doe", "1234567890")
    # Delete the existing contact
    address_book.delete_contact("John Doe")
    # Assert that the contact has been deleted from the address book
    assert "John Doe" not in address_book.contacts

# Test case to check if a non-existent contact returns an appropriate message when attempting to delete it
def test_delete_nonexistent_contact(address_book):
    # Attempt to delete a non-existent contact
    assert address_book.delete_contact("Nonexistent") == "Contact 'Nonexistent' not found!"

# Test case to check if the address book correctly lists contacts when it is empty
def test_list_contacts_empty(address_book, capsys):
    # List the contacts in the empty address book
    address_book.list_contacts()
    # Capture the output printed to the terminal
    captured = capsys.readouterr()
    # Assert that the appropriate message for an empty address book is present in the captured output
    assert "Contacts:" in captured.out
    assert "No contacts found" in captured.out

# Test case to check if the address book correctly lists contacts when it is non-empty
def test_list_contacts_nonempty(address_book, capsys):
    # Add contacts to the address book
    address_book.add_contact("John Doe", "1234567890")
    address_book.add_contact("Jane Smith", "9876543210")
    # List the contacts in the address book
    address_book.list_contacts()
    # Capture the output printed to the terminal
    captured = capsys.readouterr()
    # Assert that the contacts are correctly listed in the captured output
    assert "Contacts:" in captured.out
    assert "Name: John Doe, Phone: 1234567890" in captured.out
    assert "Name: Jane Smith, Phone: 9876543210" in captured.out

# Check if the script is being run directly, and if so, execute the pytest tests
if __name__ == "__main__":
    pytest.main()
