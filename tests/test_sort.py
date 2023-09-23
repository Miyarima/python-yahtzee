#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the Sorted class """

import unittest
from src.sort import recursive_insertion
from src.unorderedlist import UnorderedList

class TestDie(unittest.TestCase):
    """
    Class for testing the Sorted class
    """

    def test_ul_sorted_int(self):
        """ Checkin if the ul gets sorted """
        ul = UnorderedList()
        ul.append(5)
        ul.append(1)
        ul.append(15)
        ul.append(10)
        recursive_insertion(ul)
        self.assertEqual(ul.get(0), 1, "The ul is not sorted")
        self.assertEqual(ul.get(3), 15, "The ul is not sorted")

    def test_ul_sorted_str(self):
        """ Checkin if the ul gets sorted """
        ul = UnorderedList()
        ul.append("hello world")
        ul.append("are you sure?")
        ul.append("home alone")
        ul.append("x-ray")
        recursive_insertion(ul)
        self.assertEqual(ul.get(0), "are you sure?", "The ul is not sorted")
        self.assertEqual(ul.get(3), "x-ray", "The ul is not sorted")
