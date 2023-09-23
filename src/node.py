"""
This is a module containing the node class
"""

class Node:
    """ The Node class """
    def __init__(self, value):
        self.data = value
        self.next = None

    def has_next(self):
        """ Returns true if the node has a next node """
        return self.next is not None
