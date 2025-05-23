"""
Problem 6: Unsorted Integer Array

In this problem, we will look for smallest and largest integer from a list of 
unsorted integers. The code should run in O(n) time. Do not use Python's 
inbuilt functions to find min and max.

You should implement the function body according to the get_min_max function 
signature. Use the test cases provided below to verify that your algorithm is 
correct. If necessary, add additional test cases to verify that your algorithm 
works correctly.
"""

from typing import Optional

def get_min_max(ints: list[int]) -> Optional[tuple[int, int]]:
    """
    Return a tuple (min, max) from an unsorted list of integers.
    
    Args:
    ints (list[int]): A list of integers (can be empty)

    Returns:
    Optional[tuple[int, int]]: Tuple of (min, max) or None if the list is empty
    """
    if not ints:
        return None

    min_val = max_val = ints[0]

    for num in ints[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return (min_val, max_val)

# Test cases
if __name__ == '__main__':
    # Edge case: Empty input list
    print(get_min_max([]))  # Expected output: None

    # Normal case: list with negative and positive numbers
    print(get_min_max([-10, 0, 10, -20, 20]))  # Expected output: (-20, 20)

    # Normal case: list with large range of numbers
    print(get_min_max([1000, -1000, 500, -500, 0]))  # Expected output: (-1000, 1000)

    # Normal case: list with already sorted numbers
    print(get_min_max([1, 2, 3, 4, 5]))  # Expected output: (1, 5)

    # Edge case: single element list
    print(get_min_max([7]))  # Expected output: (7, 7)
