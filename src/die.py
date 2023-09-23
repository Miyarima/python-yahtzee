"""
This is a module containing the Die class
"""
import random

class Die:
    """
    This class initializes a die
    value. It also contains five
    methods, two public attributes
    and two private.
    """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6
    _names = ["one", "two", "three", "four", "five", "six"]
    _images = [
        'img/one.png',
        'img/two.png',
        'img/three.png',
        'img/four.png',
        'img/five.png',
        'img/six.png'
    ]

    def __init__(self, value = None):
        if value is None:
            self._value = random.randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)
        elif Die.MIN_ROLL_VALUE <= value <= Die.MAX_ROLL_VALUE:
            self._value = value
        elif value > Die.MAX_ROLL_VALUE:
            self._value = Die.MAX_ROLL_VALUE
        elif value < Die.MIN_ROLL_VALUE:
            self._value = Die.MIN_ROLL_VALUE

    def get_name(self):
        """ This method returns the die name on the position of the value """
        return Die._names[self.value-1]

    @property
    def value(self):
        """ This method returns the value of the die """
        return self._value

    def get_image(self):
        """ This metod returns the image corresponding to the value of the die """
        return self._images[self.value-1]

    def roll(self):
        """ This function rerolls the value of the die """
        self._value = random.randint(Die.MIN_ROLL_VALUE, Die.MAX_ROLL_VALUE)

    def __eq__(self, other):
        """ Check if the value is the same """
        try:
            if self.value == other.value:
                return True
        except AttributeError:
            if self.value == other:
                return True
        return False

    def __str__(self):
        return str(self.value)
