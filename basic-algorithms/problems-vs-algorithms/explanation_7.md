## Reasoning Behind Decisions

To solve the problem of request routing, I chose a Trie (also called a prefix tree) as the primary data structure. This is ideal for route lookups because:

* Each level in the Trie represents a segment of the path, which naturally maps to how URLs are structured.

* Tries support fast prefix-based matching, which is essential when handling nested or hierarchical URL paths like /home/about.

* Using a RouteTrie allows for efficient insertion and lookup of routes without scanning the entire route table.

Additionally, I included a Router class as an abstraction layer. This class manages URL normalization (e.g., stripping trailing slashes) and delegates storage and retrieval to the underlying Trie structure. It also supports a not found handler for unmatched routes, a common behavior in web servers.

## Efficiency

### Time Complexity

* Insertion (add_handler):
    Each path is split into k segments and inserted one-by-one into the Trie.

        Time: O(k), where k is the number of parts in the path.

* Lookup (lookup):
    Follows the same process as insertion—traverse each segment of the path to find the handler.

        Time: O(k)

Both operations are linear in the number of segments in the path, which is efficient given that URL depth is typically shallow in real-world applications.

### Space Complexity

    The Trie stores nodes for every unique segment across all routes.

        In the worst case (every route has unique segments), space is O(n × k), where:

* n is the number of routes

* k is the average number of parts per route

    Each node may also store a handler (only for complete paths), so overall memory usage is reasonable and scalable.

## Final Thoughts

This solution mimics real-world HTTP routers while maintaining clean separation of concerns:

    The RouteTrie handles structure and storage.

    The Router manages interaction and interface-level logic.

It also ensures:

    Robust handling of edge cases (e.g., root path, trailing slashes)

    Efficient matching performance for dynamic or nested paths

Using a Trie for URL routing provides clarity, performance, and maintainability—making it a practical solution for web infrastructure.
