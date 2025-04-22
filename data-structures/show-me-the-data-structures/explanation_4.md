
## Reasoning Behind Decisions:

To determine whether a user exists in a given group or any of its nested subgroups, I used an **iterative depth-first search (DFS)** with a stack. This avoids potential stack overflow issues that could occur with very deep recursion.

The search algorithm works as follows:
- Start with the given group.
- Check whether the user exists in the group’s direct user list.
- If not, add all of the group’s subgroups to a stack and continue checking.
- Repeat this process until the user is found or all groups have been explored.

This approach is efficient, simple, and scales well with deep and broad group hierarchies.


## Time Efficiency:

Let:
- `n` be the number of groups in the entire directory tree.
- `k` be the average number of users per group.

In the **worst case**, the function visits every group and checks every user list.

- **Group traversal (DFS):** O(n)
- **User lookup per group:** O(k)
- **Total worst-case time complexity:** **O(n × k)**

If the user is found early, the function exits early, making the average case more efficient.

## Space Efficiency:

- A stack is used to hold groups during traversal.
- In the worst case (e.g., all subgroups are nested), the stack holds O(n) group references.
- The function does not create any unnecessary structures besides the stack.

**Worst-case space complexity:** **O(n)**  
This is acceptable and efficient for large hierarchical structures.
