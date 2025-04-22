
## Reasoning Behind Decisions:

To implement Huffman coding efficiently, I used a min-heap (priority queue) to build the Huffman Tree. This is the standard and optimal approach for constructing a tree based on character frequencies:

* Each node contains a character and its frequency.

* The two nodes with the lowest frequencies are repeatedly merged into a parent node.

* This ensures that frequently used characters get shorter binary codes, and rare characters get longer codes.

I chose a recursive depth-first traversal to generate binary codes by assigning:

* '0' for left edges

* '1' for right edges

For decoding, I simply traverse the tree bit by bit until I reach a leaf node, collecting the corresponding character.

The solution cleanly separates concerns:

* Frequency calculation

* Tree construction

* Code generation

* Encoding and decoding logic

This modular approach improves clarity, maintainability, and testability.

## Time Efficiency:

Let n be the number of unique characters, and L be the length of the input string.

* Frequency calculation: O(L) — we scan the entire string once.

* Building the heap: O(n) to heapify the initial list of nodes.

* Huffman Tree construction: O(n log n) — each of the n-1 merges involves heap operations.

* Code generation (DFS): O(n) — we visit every node in the tree once.

* Encoding the string: O(L) — we loop over the string and replace each char with its code.

* Decoding the string: O(L) — each bit leads us through the tree to a leaf.

Total time complexity:

* Encoding: O(L + n log n)

* Decoding: O(L)

## Space Efficiency:

* Frequency dictionary: O(n)

* Heap and Huffman tree: O(n)

* Code map (dictionary of binary codes): O(n)

* Encoded string: O(L)

* Decoded string: O(L)

Total space complexity: O(n + L)

This is optimal for a lossless compression algorithm — we store only what’s necessary to encode and decode the input.
