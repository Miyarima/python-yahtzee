"""
This is a module containing all Classes for rules
"""

from abc import ABC, abstractmethod

class Rule(ABC):
    """ Abstract Class """
    @abstractmethod
    def points(self, hand):
        """ Required Method """
        # pass

class SameValueRule(Rule):
    """ Parent class for classes with the same rules """
    def __init__(self, value, name):
        self.name = name
        self.value = value
        self.__score_sum = 0

    def points(self, hand):
        """ Calculates the sum """
        for die in hand.dice:
            if die.value == self.value:
                self.__score_sum += die.value
        return self.__score_sum

class Ones(SameValueRule):
    """ Ones Class """
    def __init__(self):
        super().__init__(1, "Ones")

class Twos(SameValueRule):
    """ Twos Class """
    def __init__(self):
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    """ Threes Class """
    def __init__(self):
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    """ Fours Class """
    def __init__(self):
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    """ Fives Class """
    def __init__(self):
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    """ Sixes Class """
    def __init__(self):
        super().__init__(6, "Sixes")

class ThreeOfAKind(Rule):
    """ The Class for Three of a kind """
    _numbers = [1,2,3,4,5,6]
    def __init__(self):
        self.name = "Three Of A Kind"
        self._count = []
        self._sum = 0

    def points(self, hand):
        """
        Checks if there are 3 or more of
        the same dice, and returns the sum
        if it's true.
        """
        for i in range(6):
            for die in hand.dice:
                if die.value == self._numbers[i]:
                    self._count.append(die.value)
            if len(self._count) >= 3:
                for die in hand.dice:
                    self._sum += die.value
                return self._sum
            self._count = []
        return self._sum

class FourOfAKind(Rule):
    """ The Class for Four of a kind """
    _numbers = [1,2,3,4,5,6]
    def __init__(self):
        self.name = "Four Of A Kind"
        self._count = []
        self._sum = 0

    def points(self, hand):
        """
        Checks if there are 4 or more of
        the same dice, and returns the sum
        if it's true.
        """
        for i in range(6):
            for die in hand.dice:
                if die.value == self._numbers[i]:
                    self._count.append(die.value)
            if len(self._count) >= 4:
                for die in hand.dice:
                    self._sum += die.value
                return self._sum
            self._count = []
        return self._sum


class FullHouse(Rule):
    """ The Class for Full House """
    _numbers = [1,2,3,4,5,6]
    def __init__(self):
        self.name = "Full House"
        self._count = 0
        self._full_house = 0
        self._in_full_house = 0

    def points(self, hand):
        """
        If two dies and three dies are the same,
        returns 25.
        """
        for i in range(6):
            for die in hand.dice:
                if die.value == self._numbers[i]:
                    self._count += 1
            if self._count == 3 and self._in_full_house != 3:
                self._full_house += 1
                self._in_full_house = 3
            elif self._count == 2 and self._in_full_house != 2:
                self._full_house += 1
                self._in_full_house = 2
            self._count = 0
        if self._full_house == 2:
            return 25
        return 0

class SmallStraight(Rule):
    """ The Class for Small Straight """
    def __init__(self):
        self.name = "Small Straight"
        self._count_straight = 1
        self._last_number = 0
        self._lowest = 0

    def _lowest_value(self, hand):
        """ Finds the smallest number """
        self._lowest = hand.dice[0].value
        for _ in range(5):
            for die in hand.dice:
                if die.value < self._lowest:
                    self._lowest = die.value
        return self._lowest

    def _check_values(self, hand):
        """
        Counts the amount of values that matches a
        small straight
        """
        for _ in range(5):
            for die in hand.dice:
                if die.value == self._last_number + 1:
                    self._last_number = die.value
                    self._count_straight += 1

    def points(self, hand):
        """ Returns 40 if it contains a small straight """
        self._last_number = self._lowest_value(hand)
        for i in range(3):
            if i > 0:
                self._last_number += 1
            self._check_values(hand)
            if self._count_straight >= 4:
                return 30
            self._count_straight = 0
        return 0

class LargeStraight(Rule):
    """ The Class for Large Straight """
    def __init__(self):
        self.name = "Large Straight"
        self._count_straight = 1
        self._last_number = 0
        self._lowest = 0

    def _lowest_value(self, hand):
        """ Finds the smallest number """
        self._lowest = hand.dice[0].value
        for _ in range(5):
            for die in hand.dice:
                if die.value < self._lowest:
                    self._lowest = die.value
        return self._lowest

    def points(self, hand):
        """ If it's a straight, returns 40 """
        self._last_number = self._lowest_value(hand)
        for _ in range(5):
            for die in hand.dice:
                if die.value == self._last_number + 1:
                    self._last_number = die.value
                    self._count_straight += 1
        if self._count_straight == 5:
            return 40
        return 0

class Yahtzee(Rule):
    """ The Class for Yahtzee """
    _numbers = [1,2,3,4,5,6]
    def __init__(self):
        self.name = "Yahtzee"
        self._count = 0

    def points(self, hand):
        """ If all dices are the same, returns 50 """
        for i in range(6):
            for die in hand.dice:
                if die.value == self._numbers[i]:
                    self._count += 1
            if self._count == 5:
                return 50
            self._count = 0
        return 0

class Chance(Rule):
    """ The Class for Chance """
    def __init__(self):
        self.name = "Chance"
        self._sum = 0

    def points(self, hand):
        """ Returns the sum of all dices """
        for die in hand.dice:
            self._sum += die.value
        return self._sum
