## Reasoning Behind Decisions:

To solve this problem efficiently and in a single traversal, I implemented the Dutch National Flag algorithm, which uses three pointers (low, mid, and high) to partition the array into three sections:

* Values before low are all 0s.

* Values between low and mid are all 1s.

* Values after high are all 2s.

This technique ensures that each element is considered only once, making it a true single-pass solution.

By using in-place swaps, this method avoids extra space and follows the problem constraints: no built-in sorting, and constant auxiliary space.

This algorithm is both optimal and elegant for this specific problem domain, which only includes 0s, 1s, and 2s.

## Time Efficiency:

* We iterate through the list only once:
    \[ \text{Time Complexity} = O(n) \]
    where \( n \) is the number of elements in the input list.

## Space Efficiency:

* We use a constant number of pointers (three integers):
    \[ \text{Space Complexity} = O(1) \]
    No extra arrays or dynamic memory allocation is needed.
