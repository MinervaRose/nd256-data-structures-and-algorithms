
## Reasoning Behind Decisions:

I implemented the blockchain using a **linked-list-like approach** with a Python list for simplicity. Each `Block` object contains:

- A **timestamp** (for record-keeping and uniqueness),
- **Data** (which could represent transactions or any message),
- A **SHA-256 hash** of the block contents (including the previous block’s hash).

This creates a **tamper-evident structure**, since each block's hash depends on the previous block. If one block is altered, all subsequent hashes break.

The first block, the **genesis block**, is hard-coded with no parent hash. Every new block uses the hash of the most recent block as its `previous_hash`, chaining them together securely.

I used Python’s built-in `hashlib` for efficient SHA-256 hashing, and `datetime` for timestamp generation in UTC.

The blockchain is stored in a list rather than a manual linked list for easier iteration and printing, while still maintaining the integrity of a singly-linked structure.

## Time Efficiency:

Let:
- `n` be the number of blocks added,
- `d` be the length of the data string in a block.

- **Block creation (`add_block`)**: O(d)
  - Hashing takes O(d) time since all content (timestamp + data + previous hash) is hashed.
- **Adding a block to the chain**: O(1) (list append)
- **Creating the genesis block**: O(1)
- **Total time to build blockchain with `n` blocks**: **O(n × d)**

Efficient for appending new blocks one-by-one.

## Space Efficiency:

- Each block stores its own data, timestamp, and hash: O(d) per block.
- Blockchain stores `n` such blocks in a list.

**Total space complexity:** **O(n × d)**  
This includes:
- Block data
- Timestamps
- Hashes
- Linkage via `previous_hash`



The structure is clean, testable, scalable, and meets all functional and performance expectations for a basic blockchain simulation.

