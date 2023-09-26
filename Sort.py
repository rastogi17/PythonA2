from abc import ABC, abstractmethod
import time

class SortError(Exception):
    """Custom exception for sorting errors."""
    pass


class Sort(ABC):
    """Abstract base class for sorting algorithms."""

    def __init__(self, items):
        """Initialize a Sort instance with a list of items to be sorted.

        Args:
            items (list): The list of items to be sorted.
        """
        self._items = items

    @abstractmethod
    def _sort(self):
        """Sorts the list of items in ascending order.

        This method should be implemented by concrete sorting algorithms.

        Returns:
            list: The sorted list of items.
        """
        pass

    def get_items(self):
        """Get the original list of items.

        Returns:
            list: The original list of items.
        """
        return self._items

    def _time(self):
        """Get the time taken to execute the sorting algorithm.

        Returns:
            float: The time taken in seconds.
        """
        self.time = 0
        return self.time

class BubbleSort(Sort):
    """Implementation of the Bubble Sort algorithm."""

    def _sort(self):
        """Sorts the list of items using the Bubble Sort algorithm.

        Returns:
            list: The sorted list of items.
        """
        try:
            start_time = time.time()
            items = self._items.copy()

            n = len(items)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if items[j] > items[j + 1]:
                        items[j], items[j + 1] = items[j + 1], items[j]

            end_time = time.time()
            self.time = end_time - start_time

            return items
        except Exception as e:
            raise SortError(f"Error while sorting: {str(e)}")

    def _time(self):
        """Get the time taken to execute the Bubble Sort algorithm.

        Returns:
            float: The time taken in seconds.
        """
        return self.time

class MergeSort(Sort):
    """Implementation of the Merge Sort algorithm."""

    def _sort(self):
        """Sorts the list of items using the Merge Sort algorithm.

        Returns:
            list: The sorted list of items.
        """
        try:
            start_time = time.time()
            items = self._items.copy()

            def merge_sort(arr):
                if len(arr) <= 1:
                    return arr

                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]

                left = merge_sort(left)
                right = merge_sort(right)

                return merge(left, right)

            def merge(left, right):
                result = []
                i = j = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        result.append(left[i])
                        i += 1
                    else:
                        result.append(right[j])
                        j += 1

                result.extend(left[i:])
                result.extend(right[j:])
                return result

            sorted_items = merge_sort(items)

            end_time = time.time()
            self.time = end_time - start_time

            return sorted_items
        except Exception as e:
            raise SortError(f"Error while sorting: {str(e)}")

    def _time(self):
        """Get the time taken to execute the Merge Sort algorithm.

        Returns:
            float: The time taken in seconds.
        """
        return self.time
