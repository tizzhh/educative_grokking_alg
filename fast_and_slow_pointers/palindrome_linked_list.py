class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        result = ""
        temp = self
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


def reverse_linked_list(ptr: LinkedListNode):
    prev = None
    curr = ptr
    next = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def palindrome(head: LinkedListNode) -> bool:
    slow, fast = head, head
    count = 0
    while fast is not None and fast.next is not None:
        count += 1
        slow, fast = slow.next, fast.next.next

    mid = slow
    fast, slow = reverse_linked_list(slow), head
    for _ in range(count):
        if slow.data != fast.data:
            reverse_linked_list(fast)
            return False
        slow, fast = slow.next, fast.next
    reverse_linked_list(fast)
    return True


lst = LinkedList()
lst.create_linked_list([1, 2, 3, 4, 5])
print(palindrome(lst.head))
print(lst)
