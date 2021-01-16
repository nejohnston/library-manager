"""
COMP 1510 - Assignment 2
Author: Nicholas Johnston
Stu#: A01242666
Date: November 18, 2020
"""
from unittest import TestCase
from unittest.mock import patch

from utilities import input_check


class TestInputCheck(TestCase):
    @patch('builtins.input', side_effect=['0'])
    def test_input_check_correct_input(self, mock_input):
        message = "A menu with three options\n"
        actual = input_check(message, 3)
        expected = 0
        self.assertEqual(actual, expected)
