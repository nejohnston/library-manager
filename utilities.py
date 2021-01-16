"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 11, 2020
"""
import constants


def get_new_book_location():
    """
    Check if the inputted location is valid.

    :precondition: alpha values must be entered exactly as they appear in menu list
    :precondition:
    :postcondition: will return either an error message or a valid location
    :return: a string of a valid location
    """
    try:
        new_location = input(f'Which location would you like to move it to?\n'
                             f'To move a book, enter the shelf number or type the location.\n\n'
                             f'{constants.FILE_LOCATIONS_INTERACTION()}')
        if new_location not in constants.FILE_LOCATIONS_COMPARISON():
            raise ValueError
        return new_location
    except ValueError:
        print('That is not a valid location, please try again.')


def format_search_categories(book_categories: list):
    """
    Format the valid categories from which to search.

    :param book_categories: list of strings
    :precondition: list containing book categories
    :postcondition: formatted string containing valid categories
    :return: string of categories
    >>> categories = ['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject']
    >>> format_search_categories(categories)
    '\\n\\t0 : Author\\n\\t1 : Title\\n\\t2 : Publisher\\n\\t3 : Shelf\\n\\t4 : Category\\n\\t5 : Subject\\n'
    """
    formatted_categories = "\n"
    categories_dict = list(enumerate(book_categories))
    for key, category in categories_dict:
        formatted_categories += f"\t{key} : {category}\n"
    return formatted_categories


def format_search_results(search_results):
    """
    Format individual search results

    :param search_results: dictionary
    :postcondition: formats dictionary of search results
    >>> results = {0: ['Hughes', 'Barcelona', 'Vintage', '5', 'History', 'European']}
    >>> format_search_results(results)
    <BLANKLINE>
    These books match your search!
    <BLANKLINE>
    0 : Barcelona by Hughes
    """
    print('\nThese books match your search!\n')
    for key, book_information in search_results.items():
        print('{0} : {1} by {2}'.format(key, book_information[1], book_information[0]))
    return


def format_book_values(search_result: list):
    """
    Format the book the user chooses.

    This is different from the selection process as this provides all the information.

    :param search_result: list
    :precondition: search_result is a list of 6 strings
    :postcondition: formatted string containing book values
    """
    print("\nYou selected:\n\n\t{0} by {1}\n".format(search_result[1], search_result[0]))
    print("Book Info:\n")
    print("\tPUBLISHER: {0}\n\tSHELF:     {1}\n\tCATEGORY:  {2}\n\tSUBJECT:   {3}"
          .format(search_result[2], search_result[3], search_result[4], search_result[5]))
    return


def format_book_row(book_values: list):
    """
    Format a book (row) into original format to be written to file

    :param book_values: list
    :precondition: book_values is a list of 6 strings
    :postcondition: correctly formed book row
    :return: a book string
    >>> values = ['Hughes', 'Barcelona', 'Vintage', '5', 'History', 'European']
    >>> format_book_row(values)
    'Hughes\\tBarcelona\\tVintage\\t5\\tHistory\\tEuropean'
    """
    return f"{book_values[0]}\t{book_values[1]}\t{book_values[2]}\t" \
           f"{book_values[3]}\t{book_values[4]}\t{book_values[5]}"


def handle_search_results(search_results):
    """
    Handle user's search results

    Receives search_results, formats them, gets user input for which book they'd like to choose from the search_results,
    then formats the selected book.

    :postcondition: dictionary of keys, and the values are book values
    :return: dictionary of book values
    """
    try:
        if len(search_results) == 0:
            raise ValueError
        else:
            format_search_results(search_results)
            search_output = search_results[input_check("Please enter the key of the book you'd like to select.\n",
                                                       len(search_results))]
            format_book_values(search_output)
            return search_output
    except ValueError:
        print('Sorry, that input produces nothing.\nPlease try again.')


def get_menu_interaction():
    """
    Read main_menu_interaction.txt

    The return on this function uses input_check as a validator, this

    :postcondition:
    :return: valid menu input
    """
    with open(constants.FILE_MENU_TEXT(), 'r') as fileobject:
        return input_check(fileobject.read(), 3)


def input_check(input_message: str, menu_length: int):
    """
    Check if correct input

    All my menus are key, value pairs; the keys always being type int.
    
    :param input_message: string
    :param menu_length: int
    :precondition: menu_length is the correct length of possible inputs.
    :postcondition: returns a validated input or error message
    :return: valid int input
    """
    while True:
        try:
            user_input = int(input(f"\n{input_message}\n"))
            # Chris, if you see this, I'd like to talk to you about this function
            # list(range(0, menu_length + 1))[int(user_input)]
            if int(user_input) >= menu_length:
                raise IndexError
            return user_input
        except (IndexError, ValueError, TypeError, KeyError):
            print('That is an invalid input, please try again.')


def to_write_format(books: list):
    """
    Format the entire book collection to original format

    :param books: list of lists
    :precondition: books is a list of lists containing strings
    :postcondition: well formed string of book_values
    :return: a string containing entire book_collection
    >>> all_books = [['Hughes', 'Barcelona', 'Vintage', '5', 'History', 'European']]
    >>> to_write_format(all_books)
    'Hughes\\tBarcelona\\tVintage\\t5\\tHistory\\tEuropean\\r\\n'
    """
    book_file_string = ''
    for book in books:
        book_file_string += format_book_row(book)
    return book_file_string


def terminate_system(books_file):
    """
    Write a well formed string to the original file.

    :param books_file: list of lists
    :precondition: books_file is a string of well formed book values
    :postcondition: writes values to a file
    """
    file_string = to_write_format(books_file)
    with open(constants.FILE_BOOKS(), 'w', encoding='utf-16') as file_object:
        file_object.write(file_string)


def books_data():
    """
    Open Books_UTF.txt

    :precondition: filename must reference a valid UTF-16 file.
    :postcondition: returns a list of lists containing complete book_collection
    :return: list of lists
    """
    with open(constants.FILE_BOOKS(), 'r', encoding='utf-16', newline='') as fileobject:
        return list(book.split('\t') for book in fileobject)
