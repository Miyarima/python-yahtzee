#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the Scoreboard class """

import unittest
from src.scoreboard import Scoreboard
from src.hand import Hand

class TestDie(unittest.TestCase):
    """
    Class for testing the Scoreboard class
    """

    def test_add_points(self):
        """ Adding points to scoreboard """
        sb = Scoreboard()
        hand = Hand([1,2,1,1,1])
        sb.add_points("Ones", hand)
        self.assertEqual(sb.get_points("Ones"), 4, "The rule is not being added")

    def test_add_points_exception(self):
        """ Adding points to scoreboard """
        sb = Scoreboard()
        hand = Hand([1,2,1,1,1])
        sb.add_points("Ones", hand)
        with self.assertRaises(ValueError) as _:
            sb.add_points("Ones", hand)
