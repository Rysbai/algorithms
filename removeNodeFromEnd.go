package main

import (
	"fmt"
)

//  Definition for singly-linked list.
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

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	nodesLen := lenListNode(head)

	if nodesLen == 0 {
		return head
	}
	deleteIndex := nodesLen - n

	if deleteIndex == 0 {
		return head.Next
	}

	prevNode := head
	currentNode := head.Next

	i := 1
	for {
		if i == deleteIndex {
			prevNode.Next = currentNode.Next

			return head
		}
		prevNode = currentNode
		currentNode = currentNode.Next
		i++
	}
}

func main() {
	thrid := ListNode{3, nil}
	second := ListNode{2, &thrid}
	first := ListNode{1, &second}

	fmt.Println(removeNthFromEnd(&first, 2))
}
