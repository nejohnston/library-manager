"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 18, 2020
"""
from unittest import TestCase

from utilities import format_search_categories


class TestFormatSearchCategories(TestCase):
    def test_format_search_categories(self):
        book_categories = ['Author',
                           'Title',
                           'Publisher',
                           'Shelf',
                           'Category',
                           'Subject']
        actual = format_search_categories(book_categories)
        expected = "\n\t0 : Author\n" \
                   "\t1 : Title\n" \
                   "\t2 : Publisher\n" \
                   "\t3 : Shelf\n" \
                   "\t4 : Category\n" \
                   "\t5 : Subject\n"
        self.assertEqual(actual, expected)
