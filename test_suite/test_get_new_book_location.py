"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 17, 2020
"""
import io
from unittest import TestCase
from unittest.mock import patch

from utilities import get_new_book_location


class TestGetNewBookLocation(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_get_new_book_location_shelf(self, mock_input):
        actual = get_new_book_location()
        expected = '1'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Reading'])
    def test_get_new_book_location_not_shelf(self, mock_input):
        actual = get_new_book_location()
        expected = 'Reading'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_new_book_location_incorrect_input(self, mock_stdout, mock_input):
        get_new_book_location()
        expected = 'That is not a valid location, please try again.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=['10'])
    def test_get_new_book_location_double_digit_shelf(self, mock_input):
        actual = get_new_book_location()
        expected = '10'
        self.assertEqual(actual, expected)
