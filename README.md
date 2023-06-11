# phone_book

Thi code is an implementation of a simple phone book application. Here's a summary of what each function does:

is_valid_phone_number(number): This function takes a phone number as input and checks if it is valid based on certain requirements. It verifies that the number contains only allowed characters (digits, hyphen, and plus sign), has at least one hyphen, does not have multiple plus signs or hyphens, and meets the length restrictions. It returns True if the number is valid, and False otherwise.

add_contact(phone_book): This function allows the user to add a contact to the phone book. It prompts the user to enter the name of the contact and their phone number. It then checks if the phone number is valid using is_valid_phone_number() and if it contains at least one hyphen. If the input is valid, it adds the contact to the phone_book dictionary with the name as the key and the phone number as the value. If the input is invalid, it displays an error message and prompts the user again.

remove_contact(phone_book): This function allows the user to remove a contact from the phone book. It prompts the user to enter the name of the contact they want to remove. If the contact exists in the phone_book dictionary, it removes the contact. Otherwise, it displays an error message.

search_contact(phone_book): This function allows the user to search for a contact in the phone book. It prompts the user to enter the name of the contact they want to search for. If the contact exists in the phone_book dictionary, it displays the name and phone number of the contact. Otherwise, it displays an error message.

view_phone_book(phone_book): This function displays the contents of the phone book in alphabetical order by name. If the phone book is not empty, it iterates over the keys (names) of the phone_book dictionary and prints the name and corresponding phone number. If the phone book is empty, it displays a message indicating that the phone book is empty.

get_valid_menu_choice(): This function prompts the user to enter their choice from a menu and validates the input. It ensures that the choice is one of the valid menu options (1-5) and returns the validated choice.

main(): This is the entry point of the program. It initializes an empty phone_book dictionary and displays a welcome message. It then enters a loop where it presents a menu of options to the user and calls the appropriate function based on the user's choice. The loop continues until the user chooses to exit the program.

Overall, the code provides a basic phone book functionality with options to add, remove, search, and view contacts.





Re
