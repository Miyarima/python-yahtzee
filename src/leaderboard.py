"""
This is a module containing the Leaderboard class
"""

from src.unorderedlist import UnorderedList

class Leaderboard:
    """  The Leaderboard class """
    def __init__(self, entries = None):
        self.entries = UnorderedList()
        if entries:
            for entry in entries:
                self.entries.append(entry + ",")

    @classmethod
    def load(cls, filename):
        """ Loads the Leaderboard from a file """
        with open(filename, "r", encoding="utf8") as f:
            file_contents = f.readline()
        file_contents = file_contents[:-1]
        file_contents = file_contents.split(',')
        return cls(file_contents)

    def save(self, filename):
        """ Saves the scoreboard to a file """
        with open(filename, 'w+', encoding="utf8") as f:
            for i in range(self.entries.size()):
                f.write(self.entries.get(i))

    def add_entry(self, name, score):
        """ Adds a new entry to the unordered list """
        self.entries.append(f"{name} {score},")

    def remove_entry(self, index):
        """ Removes an entry from the unordered list """
        print(index)
        self.entries.remove(self.entries.get(index))
