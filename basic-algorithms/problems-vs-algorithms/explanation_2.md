## Problem 2: Search in a Rotated Sorted Array – Explanation

### Reasoning Behind Decisions

To search for a number in a **rotated sorted array** with **O(log n)** time complexity, I used a **modified binary search** algorithm. A standard binary search only works on fully sorted arrays. However, in a rotated sorted array, one half is always sorted, and the other may contain the rotation point.

The algorithm works by:
- Identifying whether the **left** or **right** side is sorted,
- Narrowing the search based on where the target might lie,
- Recursively or iteratively applying this logic.

I chose this approach because it maintains logarithmic efficiency without requiring extra space or data structures. The input is already sorted (partially), so there's no need to preprocess or re-sort the array.

This strategy also ensures we can find the correct index or determine that the element doesn't exist, without traversing the whole array.



### Time Efficiency

Let **n** be the length of the input array.

- At each step, we divide the array in half.
- The decision of which half to search is based on checking the sorted segment.
- Each operation is constant time, and the array size is halved every iteration.

 **Total time complexity:**  
**O(log n)**



### Space Efficiency

- The algorithm uses only a few pointers (`left`, `right`, `mid`) for computation.
- It operates directly on the input list without copying or allocating additional memory.

**Total space complexity:**  
**O(1)**



This approach is optimal and meets all constraints: correctness, performance, and readability.
