from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items in access order.
    """

    def __init__(self, capacity: int) -> None:
        """
        Initialize the cache with a fixed capacity.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> Optional[Any]:
        """
        Retrieve the value associated with the key.
        If the key exists, mark it as recently used.
        If not, return -1 (cache miss).
        """
        if key not in self.cache:
            return -1
        # Move key to the end to show it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key: int, value: Any) -> None:
        """
        Insert or update the key-value pair in the cache.
        If the cache is full, remove the least recently used item.
        """
        if key in self.cache:
            # Update value and mark as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove the least recently used (first inserted)
            self.cache.popitem(last=False)


# Test cases
if __name__ == '__main__':

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic LRU behavior")
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1  # Hit
    assert our_cache.get(2) == 2  # Hit
    assert our_cache.get(9) == -1  # Miss

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Should be evicted
    print("Test Case 1 passed.\n")

    # Test Case 2: Edge Case - Capacity 0
    print("Test Case 2: Edge case with 0 capacity")
    zero_cache = LRU_Cache(0)
    zero_cache.set(1, "A")
    assert zero_cache.get(1) == -1  # Nothing should be stored
    print("Test Case 2 passed.\n")

    # Test Case 3: Usage pattern affects eviction
    print("Test Case 3: LRU updates on access")
    pattern_cache = LRU_Cache(2)
    pattern_cache.set(1, "X")
    pattern_cache.set(2, "Y")
    pattern_cache.get(1)  # Now 2 is least recently used
    pattern_cache.set(3, "Z")  # Evicts key 2
    assert pattern_cache.get(2) == -1
    assert pattern_cache.get(1) == "X"
    assert pattern_cache.get(3) == "Z"
    print("Test Case 3 passed.\n")

    print("All test cases passed.")
