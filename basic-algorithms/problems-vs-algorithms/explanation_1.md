## Problem 1: Square Root of an Integer – Explanation

### Reasoning Behind Decisions

To find the floor of the square root of a number efficiently, I chose to use a **binary search algorithm**. This decision was based on the need for a solution with a time complexity of **O(log n)** as specified in the project instructions.

Binary search is ideal here because the square of numbers grows monotonically — i.e., for `a < b`, we always have `a² < b²`. This means we can apply a divide-and-conquer strategy: start with a range (`0` to `n`) and repeatedly narrow it by comparing `mid²` to `n`.

If we find an exact match (`mid² == n`), we return `mid`. Otherwise, if `mid² < n`, we record `mid` as the floor candidate and move right. If `mid² > n`, we move left.

I also added a check for negative input (`number < 0`) returning `-1`, since real square roots for negative numbers are complex and not defined in the domain of this function.

### Time Efficiency

The time complexity of this algorithm is:

- **O(log n)**, where `n` is the input number.
- This is because each iteration halves the search space.

This is significantly more efficient than a linear scan, especially for large values of `n`.

### Space Efficiency

The space complexity is:

- **O(1)** because the algorithm uses a fixed number of variables regardless of the input size.
- It performs all calculations in-place without requiring any additional data structures.

### Final Thought

This approach guarantees performance and correctness for all non-negative integers. It is clean, efficient, and meets the project's expectations both in logic and complexity.
