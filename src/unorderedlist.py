"""
This is a module containing the UndorderedList class
"""

from src.node import Node
from src.errors import MissingIndex, MissingValue

class UnorderedList:
    """ The UnorderedList class """
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, data):
        """ Appends data to the end of the list """
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
        else:
            current = self.head
            while current.has_next():
                current = current.next
            current.next = tmp
        self._size += 1

    def set(self, index, data):
        """ Sets the data at the given index """
        if index < self.size():
            current = self.head
            pos = 0
            while current.has_next() and index != pos:
                current = current.next
                pos += 1
            current.data = data
        else:
            raise MissingIndex

    def size(self):
        """ Returns the size of the unordered list """
        return self._size

    def get(self, index):
        """ Returns the value of the given index """
        if index < self.size():
            current = self.head
            pos = 0
            while current.has_next() and index != pos:
                current = current.next
                pos += 1
            return current.data
        raise MissingIndex

    def index_of(self, index):
        """ Returns the index of the given value """
        current = self.head
        pos = 0
        while current.has_next() and index != current.data:
            current = current.next
            pos += 1
        if index == self.get(pos):
            return pos
        raise MissingValue

    def print_list(self):
        """ Prints the values of the unordered list """
        current = self.head
        lst_str = ""
        while current.has_next():
            lst_str += str(current.data) + " "
            current = current.next
        lst_str += str(current.data)
        print(lst_str)

    def remove(self, data):
        """ Removes the given data from the unordered list """
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
        else:
            current = self.head
            last = current
            while current.has_next() and data != current.data:
                last = current
                current = current.next
            if last.has_next():
                last.next = current.next
                self._size -= 1
            else:
                raise MissingValue
