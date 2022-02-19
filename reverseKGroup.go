package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func lenListNode(head *ListNode) int {
	currentNode := head

	count := 0

	for {
		count++

		if currentNode.Next == nil {
			return count
		}

		currentNode = currentNode.Next
	}
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	if k == 1 {
		return head
	}

	nodesLen := lenListNode(head)
	var newList *ListNode
	var newListEnd *ListNode

	index := 0
	var currentReverse *ListNode
	var currentReverseEnd *ListNode

	for {
		if head == nil {
			return newList
		}

		node := head
		head = head.Next
		index++

		if currentReverse == nil {
			if nodesLen-(index-1) < k {
				if newListEnd == nil {
					return node
				}
				newListEnd.Next = node
				return newList
			}
			currentReverse = node
			currentReverseEnd = node
		}
		node.Next = currentReverse
		currentReverse = node

		if index%k == 0 {
			if newList == nil {
				newList = currentReverse
			} else {
				newListEnd.Next = currentReverse
			}
			newListEnd = currentReverseEnd
			newListEnd.Next = nil
			currentReverse = nil
			currentReverseEnd = nil
		}
	}
}

func main() {
	fifth := ListNode{5, nil}
	fourth := ListNode{4, &fifth}
	third := ListNode{3, &fourth}
	second := ListNode{2, &third}
	first := ListNode{1, &second}

	solution := reverseKGroup(&first, 3)
	fmt.Println(solution)

	for {
		if solution == nil {
			return
		}
		fmt.Println(solution.Val)
		solution = solution.Next
	}
}
