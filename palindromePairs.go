package main

import "fmt"

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func palindromePairs(words []string) [][]int {
	var pairs [][]int
	wordsMap := make(map[string]int)

	for index, word := range words {
		reversedString := Reverse(word)

		if val, ok := wordsMap[reversedString]; ok {
			pair := []int{index, val}
			pairs = append(pairs, pair)
		}

		wordsMap[word] = index
	}

	return pairs
}

func main() {
	fmt.Println(palindromePairs([]string{"abcd", "dcba", "lls", "s", "sssll"}))
}
