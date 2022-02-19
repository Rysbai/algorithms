package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	var prev *ListNode
	first := head
	second := head.Next

	for {
		if second == nil {
			return head
		}
		fmt.Println(first.Val, second.Val)
		second.Next, first.Next = first, second.Next

		if prev == nil {
			prev = first
			head = second
		} else {
			prev.Next = second
			prev = first
		}

		first = first.Next
		if first == nil {
			return head
		}
		second = first.Next
	}
}
