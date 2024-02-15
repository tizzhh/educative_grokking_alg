from typing import Any


class LinkedListNode:
    def __init__(self, data: Any, next: 'LinkedListNode' = None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head: LinkedListNode = None

    def insert_node_at_head(self, node: LinkedListNode) -> None:
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def create_linked_list(self, lst: list[Any]) -> None:
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    def __str__(self) -> str:
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


def remove_nth_last_node(head: LinkedListNode, n: int):
    left, right = head, head
    for _ in range(n):
        right = right.next

    if right is None:
        return head.next

    while right and right.next is not None:
        left = left.next
        right = right.next

    left.next = left.next.next

    return head


lst = LinkedList()
lst.create_linked_list([69, 8, 49, 106, 116, 112])
print(lst)
lst.head = remove_nth_last_node(lst.head, 5)
print(lst)
