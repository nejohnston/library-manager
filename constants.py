"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 14, 2020
"""


def FILE_BOOKS():
    """
    Constant for filename address from which to grab book values.

    :postcondition: string containing filename containing book values
    :return: string
    """
    return 'text_files/books_utf.txt'


def FILE_MENU_TEXT():
    """
    Constant for filename address from which to get the main menu interaction text.

    :postcondition: string containing filename containing book values
    :return: string
    """
    return 'text_files/main_menu_interactions.txt'


def FILE_LOCATIONS_INTERACTION():
    """
    List of strings file locations to display to user

    :postcondition: locations are well formatted to display to user
    :return: strings to display to user
    """
    return '\tShelves 1 through 38\n' \
           '\tReading\n' \
           '\tGaby\n' \
           '\tIsland\n' \
           '\tLego\n' \
           '\tStudents\n' \
           '\tNoguchi\n'


def FILE_LOCATIONS_COMPARISON():
    """
    List of locations

    Difference between this and FILE_LOCATIONS() is that this is a list and an unpacked range object
    representing shelves.

    :postcondition: a list of valid locations that can be compared to a user input
    :return: list of strings
    """
    return [*[str(shelf_num) for shelf_num in range(1, 39)], 'Reading', 'Gaby', 'Island', 'Lego', 'Students', 'Noguchi']
