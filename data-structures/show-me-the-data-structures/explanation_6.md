## Problem 6: Union and Intersection – Explanation



###  Union Function

#### **Reasoning Behind Decisions:**

To compute the union of two linked lists, I used a **set** to store all unique values from both lists. This ensures automatic deduplication and allows O(1) lookups for inserting values.

After gathering the union of values, I created a **new linked list** and appended each item from the set.

Using a set simplifies the logic, improves readability, and ensures that the final list contains each value only once, regardless of duplicates in the original inputs.



#### **Time Efficiency:**

Let `n` and `m` be the lengths of the two linked lists.

- Traversing the first list: O(n)
- Traversing the second list: O(m)
- Inserting into the set: O(1) per element on average
- Creating the result linked list: O(n + m)

 **Total Time Complexity:** O(n + m)



#### **Space Efficiency:**

- The set stores up to (n + m) unique values → O(n + m)
- The result linked list also stores those values → O(n + m)

 **Total Space Complexity:** O(n + m)



###  Intersection Function

#### **Reasoning Behind Decisions:**

To compute the intersection, I again used sets:

1. Convert the first linked list to a set for fast lookup.
2. Convert the second linked list to a second set.
3. Use Python’s built-in set intersection to find common values.
4. Build a new linked list from the result.

This is both efficient and elegant, leveraging set operations to minimize complexity and ensure correctness.



#### **Time Efficiency:**

Let `n` and `m` be the lengths of the two linked lists.

- Traversing list 1 and inserting into a set: O(n)
- Traversing list 2 and inserting into another set: O(m)
- Performing set intersection: O(min(n, m))
- Creating the result linked list: O(k), where k is the number of shared elements

 **Total Time Complexity:** O(n + m)



#### **Space Efficiency:**

- Two sets to hold values from each list → O(n + m)
- Result linked list holds up to O(min(n, m)) values

 **Total Space Complexity:** O(n + m)



