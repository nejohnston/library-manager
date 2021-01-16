"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 18, 2020
"""
from unittest import TestCase

from utilities import format_book_row


class TestFormatBookRow(TestCase):
    def test_format_book_row_valid_book(self):
        book_values = ['Dupre', 'Skyscrapers', 'BD&L', '12', 'Architecture', '20th Century']
        expected = "Dupre\tSkyscrapers\tBD&L\t12\tArchitecture\t20th Century"
        actual = format_book_row(book_values)
        self.assertEqual(expected, actual)

    def test_format_book_row_with_a_nan_value(self):
        book_values = ['Eddings', 'Belgarath the Sorcerer', '', '34', 'Fiction', 'Fantasy']
        expected = "Eddings\tBelgarath the Sorcerer\t\t34\tFiction\tFantasy"
        actual = format_book_row(book_values)
        self.assertEqual(expected, actual)
