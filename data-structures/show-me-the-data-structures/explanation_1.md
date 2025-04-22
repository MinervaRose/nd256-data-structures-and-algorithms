
## Reasoning Behind Decisions:

I chose Python’s OrderedDict because it maintains key insertion order and allows constant-time operations for moving, inserting, and deleting elements. This makes it ideal for implementing an LRU cache that requires:

* Fast get() and set() operations

* Moving accessed items to the “most recently used” position

* Removing the least recently used item when the cache is full

These behaviors align perfectly with the characteristics of an LRU cache, and OrderedDict gives us these benefits with minimal code.

## Time Efficiency:

*get() → O(1) average time
(move_to_end() and key lookup are constant time)

* set() → O(1) average time
(key insertions/updates and popitem() are constant time)

All operations are guaranteed to run in constant time on average, which meets the performance requirement.

## Space Efficiency:

* We only store up to capacity key-value pairs.

* The cache uses an OrderedDict, which has space complexity of O(capacity).

* No extra structures are introduced.

This keeps memory usage low and directly proportional to the max number of items allowed in the cache.
