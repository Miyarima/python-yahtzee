#!/usr/bin/env python3
#pylint: disable=protected-access
""" Module for testing the Hand class """

import unittest
import random
from unittest import mock
from src.hand import Hand

class TestDie(unittest.TestCase):
    """
    Class for testing the Hand class
    """
    def setUp(self):
        random.seed("die")

    def test_creating_hand_without_arg(self):
        """ Hand without arguments """
        hand = Hand()
        self.assertEqual(hand.to_list(), [5,5,4,3,3], "This is not an istance of Hand")

    def test_creating_hand_with_arg(self):
        """ Hand with arguments """
        hand = Hand([2,3,1,5,5])
        self.assertEqual(hand.to_list(), [2,3,1,5,5], "The values are not beeing added")

    def test_rerolling_dies(self):
        """ Rerolling dies """
        hand = Hand([2,3,1,5,5])
        hand.roll()
        self.assertEqual(hand.to_list(), [5,5,4,3,3], "The values are not beeing rerolled")

    def test_rerolling_dies_with_indexes(self):
        """ Rerolling dies with indexes """
        hand = Hand([2,3,1,5,5])
        hand.roll([0,2])
        self.assertEqual(hand.to_list(), [5,3,5,5,5], "The values are not beeing rerolled")

    def test_hand_to_list(self):
        """ Rerolling dies with indexes """
        hand = Hand([2,3,1,5,5])
        self.assertEqual(hand.to_list(), [2,3,1,5,5], "The values are returned as a list")

    def test_reroll_with_mock(self):
        """ Test if we can add contact. Mock validation method. """
        hand = Hand([2,3,1,5,5])
        with mock.patch.object(random, 'randint') as rand_mock:
            rand_mock.return_value = 100
            hand.roll()
            self.assertEqual(hand.to_list(), [100,100,100,100,100], "The values are being rerolled")
