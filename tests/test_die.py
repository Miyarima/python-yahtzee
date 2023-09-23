#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the Die class """

import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """
    Class for testing the Hand class
    """
    def setUp(self):
        random.seed("die")

    def test_creating_die_without_arg(self):
        """ Die without arguments """
        a_die = Die()
        self.assertEqual(a_die.value, 5, "This is not an istance of Die")

    def test_creating_die_with_arg(self):
        """ Die with arguments """
        a_die = Die(3)
        self.assertEqual(a_die.value, 3, "This die is not equal to 3")

    def test_creating_die_with_illegal_arg(self):
        """ Die with illegal arguments """
        a_die = Die(100)
        self.assertNotEqual(a_die.value, 100, "This die is equal to 100")

    def test_creating_die_and_rerolling_value(self):
        """ Randomized value """
        a_die = Die(2)
        a_die.roll()
        self.assertEqual(a_die.value, 5, "The value is not randomzied")

    def test_creating_die_and_checking_name(self):
        """ Correct name returned """
        a_die = Die(4)
        self.assertEqual(a_die.get_name(), "four", "The name of the die is not four")

    def test_creating_die_and_converting_to_str(self):
        """ Value returned as a string """
        a_die = Die(1)
        self.assertEqual(str(a_die), "1", "The value is not returned as a string")

    def test_comparing_values_from_two_dices(self):
        """  The values gets comperd and are equal """
        die1 = Die(3)
        die2 = Die(3)
        self.assertEqual(die1 == die2, True, "The values from the dices aren't getting compared")
