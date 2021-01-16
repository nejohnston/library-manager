"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 13, 2020
"""
import io
import unittest.mock
from unittest import TestCase

from utilities import format_search_results


class TestFormatSearchResults(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_format_search_results_single_value(self, mock_stdout):
        format_search_results({0: ['Gournay et al',
                                   'AIA Guide to the Architecture of Atlanta',
                                   'University of Georgia Press',
                                   '16',
                                   'Architecture',
                                   'American Architecture\r\n']})
        expected = "\nThese books match your search!\n" \
                   "\n0 : AIA Guide to the Architecture of Atlanta by Gournay et al\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_format_search_results_n_values(self, mock_stdout):
        format_search_results({0: ['Gournay et al',
                                   'AIA Guide to the Architecture of Atlanta',
                                   'University of Georgia Press',
                                   '16',
                                   'Architecture',
                                   'American Architecture\r\n'],
                               1: ['Gournay et al',
                                   'AIA Guide to the Architecture of Atlanta',
                                   'University of Georgia Press',
                                   '16',
                                   'Architecture',
                                   'American Architecture\r\n']
                               })
        expected = "\nThese books match your search!\n" \
                   "\n0 : AIA Guide to the Architecture of Atlanta by Gournay et al" \
                   "\n1 : AIA Guide to the Architecture of Atlanta by Gournay et al\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_format_search_results_n_values_with_null_value(self, mock_stdout):
        format_search_results({0: ['Gournay et al',
                                   'AIA Guide to the Architecture of Atlanta',
                                   'University of Georgia Press',
                                   '',
                                   '',
                                   'American Architecture\r\n'],
                               1: ['Gournay et al',
                                   'AIA Guide to the Architecture of Atlanta',
                                   'University of Georgia Press',
                                   '',
                                   '',
                                   'American Architecture\r\n']
                               })
        expected = "\nThese books match your search!\n" \
                   "\n0 : AIA Guide to the Architecture of Atlanta by Gournay et al" \
                   "\n1 : AIA Guide to the Architecture of Atlanta by Gournay et al\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
