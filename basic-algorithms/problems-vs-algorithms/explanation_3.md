## Reasoning Behind Decisions:

To solve this problem, the goal is to rearrange digits from a list into two numbers such that their sum is maximized, and the number of digits in each number differs by at most one.

Since sorting is not allowed using built-in functions, I implemented a custom Merge Sort to sort the digits in descending order. Merge Sort is an efficient divide-and-conquer algorithm with a guaranteed time complexity of \( O(n \log n) \).

Once sorted, I used a greedy distribution strategy: assign the largest remaining digit to the number that currently has fewer digits. This ensures both numbers grow as evenly as possible, and the largest digits end up in the highest place values — maximizing the total sum.

This approach balances correctness, efficiency, and compliance with the project’s constraints.

## Time Efficiency:

* Sorting the input using Merge Sort: \( O(n \log n) \)

* Greedy digit assignment: \( O(n) \)

Overall Time Complexity: \( O(n \log n) \)

## Space Efficiency:

* Merge Sort recursion and arrays: \( O(n) \)

* Two output numbers as lists of digits: \( O(n) \)

Overall Space Complexity: \( O(n) \)
