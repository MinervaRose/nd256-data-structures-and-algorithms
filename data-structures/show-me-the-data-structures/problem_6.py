from typing import Optional

class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string.strip(" -> ")

    def append(self, value: int) -> None:
        if self.head is None:
            self.head = Node(value)
            return

        node: Node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self) -> int:
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    result = LinkedList()
    seen = set()

    current = llist_1.head
    while current:
        if current.value not in seen:
            seen.add(current.value)
            result.append(current.value)
        current = current.next

    current = llist_2.head
    while current:
        if current.value not in seen:
            seen.add(current.value)
            result.append(current.value)
        current = current.next

    return result

def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    result = LinkedList()
    set1 = set()

    current = llist_1.head
    while current:
        set1.add(current.value)
        current = current.next

    already_added = set()
    current = llist_2.head
    while current:
        if current.value in set1 and current.value not in already_added:
            result.append(current.value)
            already_added.add(current.value)
        current = current.next

    return result

if __name__ == "__main__":
    # Test Case 1
    print("Test Case 1")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    for i in [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]:
        linked_list_1.append(i)
    for i in [6, 32, 4, 9, 6, 1, 11, 21, 1]:
        linked_list_2.append(i)
    print("Union:", union(linked_list_1, linked_list_2))
    print("Intersection:", intersection(linked_list_1, linked_list_2))

    # Test Case 2: No common elements
    print("\nTest Case 2")
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    for i in [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]:
        linked_list_3.append(i)
    for i in [1, 7, 8, 9, 11, 21, 1]:
        linked_list_4.append(i)
    print("Union:", union(linked_list_3, linked_list_4))
    print("Intersection:", intersection(linked_list_3, linked_list_4))  # Expected: empty

    # Test Case 3: One list empty
    print("\nTest Case 3")
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()
    for i in [1, 2, 3]:
        linked_list_5.append(i)
    # linked_list_6 remains empty
    print("Union:", union(linked_list_5, linked_list_6))  # Expected: 1 -> 2 -> 3
    print("Intersection:", intersection(linked_list_5, linked_list_6))  # Expected: empty

    # Test Case 4: Both lists empty
    print("\nTest Case 4")
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()
    print("Union:", union(linked_list_7, linked_list_8))  # Expected: empty
    print("Intersection:", intersection(linked_list_7, linked_list_8))  # Expected: empty
