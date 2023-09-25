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

class LinSearch(Sort):
    """Class that represents a LinSearch implementation."""

    def _search(self, items):
        # your code here

        return items

    def _time(self, items):
        # your code here

        return self.time

"""Module with the implementation of the BinSearch algorithm."""

class BinSearch(Search):
    """Class that represents a BinSearch implementation."""

    def _search(self, items):
        # your code here
        left, right = 0, len(self._items) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self._items[mid] == self._target:
                return mid
            elif self._items[mid] < self._target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def _time(self, items):
        # your code here

        return self.time