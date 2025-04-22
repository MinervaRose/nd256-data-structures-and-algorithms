import heapq
from collections import defaultdict
from typing import Optional

# Huffman Tree Node
class HuffmanNode:
    def __init__(self, char: Optional[str], freq: int) -> None:
        self.char = char
        self.freq = freq
        self.left: Optional[HuffmanNode] = None
        self.right: Optional[HuffmanNode] = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq


def calculate_frequencies(data: str) -> dict[str, int]:
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    return frequency


def build_huffman_tree(frequency: dict[str, int]) -> Optional[HuffmanNode]:
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    if node is None:
        return
    if node.char is not None:
        # Handle special case where code is empty (only one unique character)
        huffman_codes[node.char] = code if code != "" else "0"
        return
    generate_huffman_codes(node.left, code + "0", huffman_codes)
    generate_huffman_codes(node.right, code + "1", huffman_codes)


def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    if not data:
        return "", None

    frequency = calculate_frequencies(data)
    root = build_huffman_tree(frequency)

    huffman_codes: dict[str, str] = {}
    generate_huffman_codes(root, "", huffman_codes)

    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, root


def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    if not encoded_data or tree is None:
        return ""

    decoded = []
    node = tree

    for bit in encoded_data:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded.append(node.char)
            node = tree

    return ''.join(decoded)


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2: Empty input
    print("\nTest Case 2: Empty string")
    encoded_data, tree = huffman_encoding("")
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert decoded_data == ""

    # Test Case 3: Single character repeated
    print("\nTest Case 3: Single character repeated")
    test_string = "aaaaaaa"
    encoded_data, tree = huffman_encoding(test_string)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert decoded_data == test_string

    print("\n All test cases passed.")
