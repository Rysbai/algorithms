package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeKLists(lists []*ListNode) *ListNode {
	var mergedList *ListNode
	var lastNode *ListNode

	for {
		var minNode *ListNode
		var removedIndex int

		for index, node := range lists {
			if node == nil {
				continue
			}

			if minNode == nil || node.Val < minNode.Val {
				minNode = node
				removedIndex = index
			}
		}

		if minNode == nil {
			return mergedList
		}

		if mergedList == nil {
			mergedList = minNode
			lastNode = minNode
		} else {
			lastNode.Next = minNode
			lastNode = minNode
		}

		lists[removedIndex] = minNode.Next

	}
}
