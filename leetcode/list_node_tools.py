

class ListNode:
    def __init__(self, val, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next


    def __repr__(self) -> str:
        return f"ListNode: {self.val=}"

    def __str__(self) -> str:
        r = ""
        node = self

        while node:
            r += f"-> {node.val}"
            node = node.next

        return r


def array_to_list_node(arr: list[int]) -> ListNode:
    head = None
    tail = None

    for num in arr:
        node = ListNode(num)

        if not head:
            head = node
            tail = node
            continue

        tail.next = node
        tail = node

    return head

