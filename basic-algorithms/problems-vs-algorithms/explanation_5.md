## Reasoning Behind Decisions

To implement autocomplete, we used a Trie (prefix tree) because it is well-suited for storing a dynamic set of strings where prefix-based operations are common. Each node in the trie represents a single character and maintains a dictionary of its children.

We created two classes:

* TrieNode: represents each character and stores its children and end-of-word status.

* Trie: maintains the root node and handles word insertion and prefix lookup.

Once the trie was built, we added a suffixes() method to TrieNode. This recursive method collects all the suffixes that complete valid words starting from any given node. This supports efficient autocomplete suggestions.

This structure supports both fast word insertions and quick retrieval of all words starting with a given prefix, making it ideal for autocomplete.

## Time Efficiency

Let n be the number of characters in a word and m be the total number of nodes visited when collecting suffixes:

* Insert a word into the trie:
    O(n) time per word, since each character is inserted once.

* Finding a prefix node:
    O(n) time where n is the length of the prefix.

* Collecting suffixes from a node:
    Worst-case O(m), where m is the total number of characters in all suffixes under that node. This happens when many words share the prefix.

Autocomplete time is proportional to the number of valid completions, which is optimal.

## Space Efficiency

Each node stores:

* A children dictionary (up to 26 entries for lowercase letters).

* A Boolean flag for is_end_of_word.

The total space used is O(k), where k is the total number of characters across all inserted words. This is more space-efficient than storing all possible suffixes explicitly and allows reuse of common prefixes.
