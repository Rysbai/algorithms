# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumRootNode = None
        currentNode = None
        nextNode1 = l1
        nextNode2 = l2
        toNext = 0

        while True:
            if nextNode1 is None and nextNode2 is None and toNext == 0:
                break

            n1 = nextNode1.val if nextNode1 else 0
            n2 = nextNode2.val if nextNode2 else 0

            sumOfDigits = n1 + n2 + toNext

            if toNext > 0:
                toNext = 0

            if sumOfDigits > 9:
                sumOfDigits = sumOfDigits % 10
                toNext = 1

            node = ListNode(sumOfDigits)
            if currentNode:
                currentNode.next = node

            currentNode = node
            if not sumRootNode:
                sumRootNode = currentNode

            nextNode1 = nextNode1.next if nextNode1 else None
            nextNode2 = nextNode2.next if nextNode2 else None

        return sumRootNode


def test_1():
    l1_first = ListNode(1)
    l1_second = ListNode(2, l1_first)
    l1_third = ListNode(3, l1_second)

    l2_first = ListNode(4)
    l2_second = ListNode(5, l2_first)
    l2_third = ListNode(6, l2_second)

    solution = Solution()
    sumListNode = solution.addTwoNumbers(l1_third, l2_third)

    assert sumListNode.val == 9
    assert sumListNode.next.val == 7
    assert sumListNode.next.next.val == 5


def test_2():
    l1_first = ListNode(5)
    l1_second = ListNode(6, l1_first)
    l1_third = ListNode(9, l1_second)

    l2_first = ListNode(4)
    l2_second = ListNode(7, l2_first)
    l2_third = ListNode(9, l2_second)

    solution = Solution()
    sumListNode = solution.addTwoNumbers(l1_third, l2_third)

    assert sumListNode.val == 8
    assert sumListNode.next.val == 4
    assert sumListNode.next.next.val == 0
    assert sumListNode.next.next.next.val == 1


if __name__ == '__main__':
    test_1()
    test_2()
