"""
This is a module containing the queue class
"""

class Queue:
    """The queue class"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ Returns True if the queue is empty """
        return not self.items

    def enqueue(self, item):
        """ Enqueues the item """
        self.items.append(item)

    def dequeue(self):
        """ Dequeues the item """
        try:
            return self.items.pop(0)

        except IndexError:
            return "Empty list."

    def peek(self):
        """ Returns the first item in the queue """
        return self.items[0]

    def size(self):
        """ Returns the number of items in the queue """
        return len(self.items)

    def to_list(self):
        """ Returns the queued items """
        return self.items
