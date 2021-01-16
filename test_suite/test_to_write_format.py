"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 18, 2020
"""
from unittest import TestCase

from utilities import to_write_format


class TestToWriteFormat(TestCase):
    def test_to_write_format_single_book(self):
        single_book = [['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject\r\n']]
        actual = to_write_format(single_book)
        expected = "Author\tTitle\tPublisher\tShelf\tCategory\tSubject\r\n\r\n"
        self.assertEqual(actual, expected)

    def test_to_write_format_n_books(self):
        single_book = [['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject\r\n'],
                       ['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject\r\n']]
        actual = to_write_format(single_book)
        expected = "Author\tTitle\tPublisher\tShelf\tCategory\tSubject\r\n\r\nAuthor\tTitle\tPublisher\tShelf" \
                   "\tCategory\tSubject\r\n\r\n"
        self.assertEqual(actual, expected)
