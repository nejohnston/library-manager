"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 18, 2020
"""
import io
from unittest import TestCase
from unittest.mock import patch

from utilities import format_book_values


class TestFormatBookValues(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_format_book_values_single_book(self, mock_stdout):
        book_values = ['Gournay et al',
                       'AIA Guide to the Architecture of Atlanta',
                       'University of Georgia Press',
                       '16',
                       'Architecture',
                       'American Architecture']
        format_book_values(book_values)
        expected = '\nYou selected:\n\n\tAIA Guide to the Architecture of Atlanta by Gournay et al\n\n' \
                   "Book Info:\n\n\tPUBLISHER: University of Georgia Press\n\tSHELF:     16\n\tCATEGORY:  " \
                   "Architecture\n\tSUBJECT:   American Architecture\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_format_book_values_null_value(self, mock_stdout):
        book_values = ['Gournay et al',
                       'AIA Guide to the Architecture of Atlanta',
                       'University of Georgia Press',
                       '',
                       'Architecture',
                       'American Architecture']
        format_book_values(book_values)
        expected = '\nYou selected:\n\n\tAIA Guide to the Architecture of Atlanta by Gournay et al\n\n' \
                   "Book Info:\n\n\tPUBLISHER: University of Georgia Press\n\tSHELF:     \n\tCATEGORY:  " \
                   "Architecture\n\tSUBJECT:   American Architecture\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
