import hashlib
import datetime

class Block:
    """
    A class to represent a block in the blockchain.

    Attributes:
    -----------
    timestamp : datetime.datetime
        The timestamp when the block was created.
    data : str
        The data stored in the block.
    previous_hash : str
        The hash of the previous block in the chain.
    hash : str
        The hash of the current block.
    """

    def __init__(self, timestamp: datetime.datetime, data: str, previous_hash: str) -> None:
        """
        Constructs all the necessary attributes for the Block object.

        Parameters:
        -----------
        timestamp : datetime.datetime
            The timestamp when the block was created.
        data : str
            The data stored in the block.
        previous_hash : str
            The hash of the previous block in the chain.
        """
        self.timestamp: datetime.datetime = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()

    def calc_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.

        Returns:
        --------
        str
            The hash of the block.
        """
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        """
        Return a string representation of the block.

        Returns:
        --------
        str
            A string representation of the block.
        """
        return (f"Block(\n"
                f"  Timestamp: {self.timestamp},\n"
                f"  Data: {self.data},\n"
                f"  Previous Hash: {self.previous_hash},\n"
                f"  Hash: {self.hash}\n"
                f")\n")

class Blockchain:
    def __init__(self) -> None:
        self.chain: list[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        # Create the first block with default values
        genesis_block = Block(datetime.datetime.utcnow(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data: str) -> None:
        # The new block's previous_hash should be the last block's hash
        last_block = self.chain[-1]
        new_block = Block(datetime.datetime.utcnow(), data, last_block.hash)
        self.chain.append(new_block)

    def __repr__(self) -> str:
        return '\n'.join(str(block) for block in self.chain)

if __name__ == "__main__":
    print("Test Case 1: Basic blockchain functionality")
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    blockchain.add_block("Block 3 Data")
    print(blockchain)

    print("\nTest Case 2: Edge case with empty data")
    blockchain2 = Blockchain()
    blockchain2.add_block("")
    blockchain2.add_block("Final Block")
    print(blockchain2)

    print("\nTest Case 3: Very large data block")
    large_data = "A" * 1000000  # 1 million characters
    blockchain3 = Blockchain()
    blockchain3.add_block(large_data)
    print(f"First block in large blockchain:\n{blockchain3.chain[0]}")
    print(f"Second block (large data):\n{blockchain3.chain[1]}")
