package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func createReverse(head *ListNode) (*ListNode, int) {
	var reverseHead *ListNode
	count := 0

	for {
		if head == nil {
			return reverseHead, count
		}

		if reverseHead == nil {
			reverseHead = &ListNode{head.Val, nil}
		} else {
			oldHead := reverseHead
			reverseHead = &ListNode{head.Val, oldHead}
		}
		head = head.Next
		count++
	}
}

func pairSum(head *ListNode) int {
	reverseHead, count := createReverse(head)

	currentCount := 0
	maxSum := 0

	for {
		if currentCount >= (count / 2) {
			return maxSum
		}

		first := head.Val
		second := reverseHead.Val
		sum := first + second

		if sum > maxSum {
			maxSum = sum
		}

		head = head.Next
		reverseHead = reverseHead.Next
		currentCount++
	}
}

func main() {
	fourth := &ListNode{1, nil}
	third := &ListNode{2, fourth}
	second := &ListNode{4, third}
	first := &ListNode{5, second}
	fmt.Println(pairSum(first))
}
