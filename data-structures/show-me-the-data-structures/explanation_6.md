## Problem 6: Union and Intersection – Explanation (Updated)



### Union Function

#### **Reasoning Behind Decisions:**

To compute the union of two linked lists, I used a set to track which values had already been added. I manually traversed each list and added each value to the set **only if it hadn’t been seen before**, then appended it to a new result linked list.

This avoids using Python’s `set.union()` method and meets the requirement to manually implement the union logic while still benefiting from O(1) average-time set lookups.



#### **Time Efficiency:**

Let `n` and `m` be the lengths of the two linked lists:

- Traversing the first list: O(n)
- Traversing the second list: O(m)
- Inserting into the set and checking for duplicates: O(1) average per operation
- Appending to the result linked list: O(n + m) in total

**Total Time Complexity:** O(n + m)



#### **Space Efficiency:**

- The set stores up to (n + m) unique values → O(n + m)
- The result linked list also stores those values → O(n + m)

**Total Space Complexity:** O(n + m)



### Intersection Function

#### **Reasoning Behind Decisions:**

For the intersection, I stored values from the first list in a set to enable fast lookups. Then, I manually iterated through the second list, and for each value, checked whether it was in the set from the first list **and not already added to the result**.

This approach avoids using `set.intersection()` while still identifying common values between the lists in an efficient and readable way.


#### **Time Efficiency:**

Let `n` and `m` be the lengths of the two linked lists:

- Traverse list 1 and insert into set: O(n)
- Traverse list 2 and check each element against set: O(m)
- Prevent duplicates in output using a second set: O(1) average time per check
- Appending to the result linked list: O(k), where `k` is number of shared elements

 **Total Time Complexity:** O(n + m)



#### **Space Efficiency:**

- One set to store values from list 1 → O(n)
- One set to track already-added values in the result → O(k)
- Result linked list stores up to O(k) elements

**Total Space Complexity:** O(n + k)
