## Problem 3: Huffman Coding – Explanation (Updated)

### **Reasoning Behind Decisions:**

I implemented Huffman encoding using a min-heap (priority queue) to build the binary Huffman tree, based on character frequency. More frequent characters get shorter codes, while rarer characters get longer codes.

- I used a custom `HuffmanNode` class and Python’s built-in `heapq` module.
- To generate codes, I performed a depth-first traversal of the tree.
- For encoding, I mapped each character in the input string to its binary code.
- For decoding, I traversed the Huffman tree according to the bitstream.

#### Special case:
If the input string contains only one unique character (e.g., `"aaaaaa"`), we ensure that it is still encoded using a default code (e.g., `"0"`). During decoding, we simply repeat the character for the length of the encoded bitstring. This case required explicit handling to avoid tree traversal errors and ensure correctness.



### **Time Efficiency:**

Let `n` be the number of unique characters, and `L` the length of the input string:

- **Frequency calculation:** O(L)
- **Heap construction:** O(n)
- **Building the Huffman Tree:** O(n log n)
- **Code generation (DFS traversal):** O(n)
- **Encoding the string:** O(L)
- **Decoding the string:** O(L)

 **Total time complexity**:
- **Encoding:** O(L + n log n)
- **Decoding:** O(L)



### **Space Efficiency:**

- **Frequency dictionary:** O(n)
- **Heap / Tree structure:** O(n)
- **Huffman code map:** O(n)
- **Encoded data and decoded result:** O(L)

 **Total space complexity:** O(n + L)

This is optimal for a lossless compression algorithm and ensures linear scalability with the input.

