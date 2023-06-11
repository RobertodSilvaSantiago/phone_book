def is_valid_phone_number(number):
    """
    Check if a phone number is valid based on the specified requirements.

    Args:
        number (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """

    allowed_chars = set("0123456789-+")

    # Check if the number contains only allowed characters
    if not set(number).issubset(allowed_chars):
        return False

    # Check if the number has at least one hyphen
    if number.count("-") < 1:
        return False

    if number.count("+") > 1 or number.count("-") > 1:
        return False

    if number.startswith("+"):
        if len(number) < 7 or len(number) > 12:
            return False
        if not number[1:].replace("-", "").isdigit():
            return False
    else:
        if len(number) < 6 or len(number) > 11:
            return False
        if not number.replace("-", "").isdigit():
            return False

    return True



def add_contact(phone_book):
    """
    Add a contact to the phone book.

    Args:
        phone_book (dict): The phone book dictionary to add the contact to.
    """

    name = input("Enter the name of the contact: ")
    while True:
        number = input(f"Enter the phone number of {name}: ")
        if is_valid_phone_number(number) and "-" in number:
            phone_book[name] = number
            print("Contact added successfully!")
            break
        else:
            print("Invalid phone number. Please enter a valid phone number with at least one hyphen.")



def remove_contact(phone_book):
    """
    Remove a contact from the phone book.

    Args:
        phone_book (dict): The phone book dictionary to remove the contact from.
    """

    name = input("Enter the name of the contact to remove: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} has been removed.")
    else:
        print(f"Contact {name} not found.")


def search_contact(phone_book):
    """
    Search for a contact in the phone book.

    Args:
        phone_book (dict): The phone book dictionary to search the contact in.
    """

    name = input("Enter the name of the contact to search for: ")
    if name in phone_book:
        print(f"{name}'s phone number is {phone_book[name]}.")
    else:
        print(f"Contact {name} not found.")


def view_phone_book(phone_book):
    """
    View the contents of the phone book.

    Args:
        phone_book (dict): The phone book dictionary to view.
    """

    print("Phone Book:")
    if phone_book:
        for name in sorted(phone_book.keys()):
            print(f"- {name}: {phone_book[name]}")
    else:
        print("Phone book is empty.")


def get_valid_menu_choice():
    """
    Get a valid menu choice from the user.

    Returns:
        str: The valid menu choice.
    """

    valid_choices = {"1", "2", "3", "4", "5"}
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def main():
    """
    Run the phone book application.
    """

    phone_book = {}
    print("Welcome to the phone book app!")

    while True:
        print("\nSelect an action:")
        print("1. Add a contact")
        print("2. Remove a contact")
        print("3. Search for a contact")
        print("4. View the phone book")
        print("5. Exit")

        choice = get_valid_menu_choice()
        print()

        if choice == "1":
            add_contact(phone_book)
        elif choice == "2":
            remove_contact(phone_book)
        elif choice == "3":
            search_contact(phone_book)
        elif choice == "4":
            view_phone_book(phone_book)
        elif choice == "5":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
