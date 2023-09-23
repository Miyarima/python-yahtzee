"""
This is a module containing the Errors class
"""

class Error(Exception):
    """User defined class for custom exceptions"""

class MissingIndex(Error):
    """ The given index is missing """

class MissingValue(Error):
    """ The given value is missing """
