"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 5, 2020
"""
import utilities


def menu():
    """
    Ask for an input from the user based on main_menu_interactions.

    This function gets an input and then calls librarian if the user does not quit.

    :postcondition: while loop continues until user quits
    """
    books_file = utilities.books_data()
    while True:
        user_menu_input = utilities.get_menu_interaction()
        if user_menu_input == 2:
            print('\nHave a nice day!')
            utilities.terminate_system(books_file)
            break
        else:
            librarian(user_menu_input,
                      books_file,
                      text_to_search=input('Please enter the value you seek.\n'))


def librarian(user_main_menu_input: int, books_file: list, text_to_search: str):
    """
    Determine the action of the book: update, or search and update

    :param user_main_menu_input: input from menu()
    :param books_file: list of book collection
    :param text_to_search: user's text to search
    :precondition: book_data must be a list of books
    :postcondition: search_results will appear with matches or a helpful error message
    :return: a dictionary of search matches
    """

    def search():
        """
        Search for text_to_search in books_file

        Based on action_type the function will either search based on the category selected in main_menu or will search
        the whole file if it's to update a file. Both have the same functionality, different search parameters

        :postcondition: dictionary with values of lists containing book information
        :return: a dictionary of list values
        """
        selected_category_to_search = int(input(f"\nWhich category would you like to search?\n"
                                                f"{utilities.format_search_categories(books_file[0])}"))
        search_results = []
        for book_attributes in books_file:
            if text_to_search.lower() in book_attributes[selected_category_to_search].lower():
                search_results += [book_attributes]
        return utilities.handle_search_results(dict(enumerate(search_results)))

    def update_book_location():
        """
        Updates the book location.

        Call search, take the location value from search, update the book's previous location
        """
        book_to_update = search()
        if book_to_update:
            new_valid_location = utilities.get_new_book_location()
            correct_location = input(f"Enter y to move {book_to_update[1]} to the new location.\n")
            if correct_location == 'y':
                book_to_update[3] = new_valid_location
            else:
                print('\nThe book was not moved.\n')

    if user_main_menu_input == 1:
        update_book_location()
    else:
        search()


def main():
    """
    Drives the program.
    """
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
    menu()


if __name__ == "__main__":
    main()
