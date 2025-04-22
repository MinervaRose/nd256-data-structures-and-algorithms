### Reasoning Behind Decisions:

The goal was to find the minimum and maximum values in an unsorted list in linear time, without using Python’s built-in `min()` or `max()` functions. 

To solve this, I used a simple linear scan of the list, initializing both `min_val` and `max_val` to the first element. I then traversed the rest of the list once, updating `min_val` and `max_val` whenever a smaller or larger number was encountered, respectively.

This approach is memory-efficient, uses no extra data structures, and handles edge cases like an empty list or a single-element list gracefully.



### Time Efficiency:

Let **n** be the number of elements in the list.

- Initializing min and max: **O(1)**
- Single traversal of the list: **O(n)**

**Total Time Complexity:**  
$$O(n)$$

This is optimal since each element must be checked at least once to determine the global minimum and maximum.



### Space Efficiency:

- We only store two extra variables (`min_val`, `max_val`) regardless of input size.
- No additional data structures are used.

**Total Space Complexity:**  
$$O(1)$$
