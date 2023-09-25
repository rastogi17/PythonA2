from abc import ABC, abstractmethod

"""Module with the base implementation of a Search class."""

class Search(ABC):
    """Abstract base class for searching."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _search(self):

        pass

    def get_items(self):
        return self._items

    def _time(self):
        self.time = 0
        return self.time
    
"""Module with the implementation of the LinSearch algorithm."""

class LinSearch(Search):
    """Class that represents a LinSearch implementation."""

    def _search(self, items):
        # your code here
        for i in range(len(self._items)):
            if self._items[i] == self._target:
                return i
        return -1
    
    def _time(self, items):
        # your code here

        return self.time

"""Module with the implementation of the BinSearch algorithm."""

class BinSearch(Sort):
    """Class that represents a BinSearch implementation."""

    def _search(self, items):
        # your code here

        return False

    def _time(self, items):
        # your code here

        return self.time