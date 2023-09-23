"""
This is a module containing all Classes for rules
"""

from src.rules import Ones, Twos, Threes, Fours, Fives, Sixes
from src.rules import ThreeOfAKind, FourOfAKind, FullHouse
from src.rules import SmallStraight, LargeStraight, Yahtzee, Chance

class Scoreboard:
    """ The Scoreboard class """
    _used_rules = {}
    def __init__(self, _used_rules = None):
        if _used_rules is None:
            self._used_rules = {}
        elif _used_rules == {}:
            self._used_rules = {}
        else:
            for key, value in _used_rules.items():
                self._used_rules[key] = value

    def add_points(self, rule_name, hand):
        """ Adds points the the given rule """
        keys = self._used_rules.keys()
        func = {
            "Ones": Ones(),
            "Twos": Twos(),
            "Threes": Threes(),
            "Fours": Fours(),
            "Fives": Fives(),
            "Sixes": Sixes(),
            "Three Of A Kind": ThreeOfAKind(),
            "Four Of A Kind": FourOfAKind(),
            "Full House": FullHouse(),
            "Small Straight": SmallStraight(),
            "Large Straight": LargeStraight(),
            "Yahtzee": Yahtzee(),
            "Chance": Chance()
        }
        if rule_name not in keys:
            self._used_rules[rule_name] = func[rule_name].points(hand)
        elif self._used_rules[rule_name] == -1:
            self._used_rules[rule_name] = func[rule_name].points(hand)
        else:
            raise ValueError

    def get_total_points(self):
        """ Returns the total points """
        _points = 0
        for value in self._used_rules.values():
            if value != -1:
                _points += value
        return _points

    def get_points(self, rule_name):
        """ Returns the points of the given rule """
        if rule_name in self._used_rules:
            return self._used_rules[rule_name]
        return -1

    def get_used_rules(self):
        """ Returns used rules dict """
        return self._used_rules

    def finished(self):
        """ Checks if the game is finished """
        _completed_rules = 0
        for value in self._used_rules.values():
            if value != -1:
                _completed_rules += 1
        if _completed_rules == 13:
            return True
        return False

    @classmethod
    def from_dict(cls, points):
        """ Creates a scoreboard with a given dict """
        return cls(points)
    