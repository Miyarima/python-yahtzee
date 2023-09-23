"""
This is a module containing the Hand class
"""

from src.die import Die
# from die import Die

class Hand:
    """
    This class initializes a list
    containing the dies. It also
    contains two methods.
    """
    def __init__(self, dice = None):
        lst = []
        if dice is None:
            for _ in range(5):
                lst.append(Die())
            self.dice = lst
        else:
            for die in dice:
                lst.append(Die(die))
            self.dice = lst

    def roll(self, dice_values = None):
        """ This method rerolls all dies or the once on the given index """
        if dice_values is None:
            for die in self.dice:
                die.roll()
            return self
        for die in dice_values:
            self.dice[die].roll()
        return self

    def to_list(self):
        """ Returns a list with all die values as ints """
        dies = []
        for die in self.dice:
            dies.append(die.value)
        return dies

    def __str__(self):
        str_dies = ""
        for i, die in enumerate(self.dice):
            if i < 4:
                str_dies += str(die.value) + ", "
            else:
                str_dies += str(die.value)
        return str_dies
