
## Reasoning Behind Decisions:

I chose to implement the recursive directory traversal using os.listdir() and os.path functions instead of os.walk(), as per the problem constraints. The recursion handles both directories and files:

* If it’s a file, it checks the suffix.

* If it’s a directory, it recurses deeper.

This design ensures we cover unlimited depth and explore every folder only once.

## Time Efficiency:

Let n be the number of items in the directory tree (files + folders).

* We visit each file or directory once: O(n)

* Each string operation like .endswith() and os.path.join() is O(1)

Overall time complexity: O(n)

## Space Efficiency:

* We use extra space for the recursion stack → up to the depth of the directory tree: O(d)

* We store matching file paths in a list: O(k), where k is the number of matches

Total space complexity: O(d + k)
