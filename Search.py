from abc import ABC, abstractmethod
import time

class SearchError(Exception):
    """Custom exception for searching errors."""
    pass

class Search(ABC):
    """Abstract base class for searching algorithms."""

    def __init__(self, items, target):
        """Initialize a Search instance with a list of items and a target to search for.

        Args:
            items (list): The list of items to search within.
            target: The target item to search for.
        """
        self._items = items
        self._target = target

    @abstractmethod
    def _search(self):
        """Performs a search to find the target item.

        This method should be implemented by concrete searching algorithms.

        Returns:
            int: The index of the target item if found, -1 otherwise.
        """
        pass

    def get_items(self):
        """Get the original list of items.

        Returns:
            list: The original list of items.
        """
        return self._items

    def _time(self):
        """Get the time taken to execute the searching algorithm.

        Returns:
            float: The time taken in seconds.
        """
        self.time = 0
        return self.time

class LinSearch(Search):
    """Implementation of the Linear Search algorithm."""

    def _search(self):
        """Performs a linear search to find the target item.

        Returns:
            int: The index of the target item if found, -1 otherwise.
        """
        try:
            start_time = time.time()
            items = self._items.copy()

            for i, item in enumerate(items):
                if item == self._target:
                    end_time = time.time()
                    self.time = end_time - start_time
                    return i  # Return the index where the target was found

            end_time = time.time()
            self.time = end_time - start_time
            return -1  # Target not found
        except Exception as e:
            raise SearchError(f"Error while searching: {str(e)}")

    def _time(self):
        """Get the time taken to execute the Linear Search.

        Returns:
            float: The time taken in seconds.
        """
        return self.time

class BinSearch(Search):
    """Implementation of the Binary Search algorithm."""

    def _search(self):
        """Performs a binary search to find the target item.

        Returns:
            int: The index of the target item if found, -1 otherwise.
        """
        try:
            start_time = time.time()
            items = self._items.copy()

            left, right = 0, len(items) - 1

            while left <= right:
                mid = (left + right) // 2
                if items[mid] == self._target:
                    end_time = time.time()
                    self.time = end_time - start_time
                    return mid  # Return the index where the target was found
                elif items[mid] < self._target:
                    left = mid + 1
                else:
                    right = mid - 1

            end_time = time.time()
            self.time = end_time - start_time
            return -1  # Target not found
        except Exception as e:
            raise SearchError(f"Error while searching: {str(e)}")

    def _time(self):
        """Get the time taken to execute the Binary Search.

        Returns:
            float: The time taken in seconds.
        """
        return self.time
