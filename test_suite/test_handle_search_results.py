"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 17, 2020
"""
import io
from unittest import TestCase
from unittest.mock import patch

from utilities import handle_search_results


class TestHandleSearchResults(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_new_book_location_empty_search_results(self, mock_stdout):
        handle_search_results(search_results={})
        expected = 'Sorry, that input produces nothing.\nPlease try again.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=['0'])
    def test_get_new_book_location_single_search_result(self, mock_input):
        search_results = {0: ['Hughes', 'Barcelona', 'Vintage', '5', 'History', 'European\r\n']}
        actual = handle_search_results(search_results)
        expected = ['Hughes', 'Barcelona', 'Vintage', '5', 'History', 'European\r\n']
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['0'])
    def test_get_new_book_location_n_search_results(self, mock_input):
        search_results = {0: ['Hughes', 'Barcelona', 'Vintage', '5', 'History', 'European\r\n'],
                          1: ['Hughes', 'Barcelona', 'Vintage', '5', 'History', 'European\r\n']}
        actual = handle_search_results(search_results)
        expected = ['Hughes', 'Barcelona', 'Vintage', '5', 'History', 'European\r\n']
        self.assertEqual(actual, expected)
