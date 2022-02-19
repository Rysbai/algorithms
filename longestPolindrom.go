package main

import (
	"fmt"
)

func ReverseWord(word string) string {
	runes := []rune(word)
	runes[0], runes[1] = runes[1], runes[0]

	return string(runes)
}

func longestPalindrome(words []string) int {
	wordsMap := make(map[string]int)
	palindromLen := 0

	for _, word := range words {
		mirror := ReverseWord(word)

		if val, ok := wordsMap[mirror]; ok {
			if val >= 1 {
				palindromLen += 4
				wordsMap[mirror]--
				continue
			}
		}

		if _, ok := wordsMap[word]; ok {
			wordsMap[word]++
			continue
		}
		wordsMap[word] = 1
	}

	for key, value := range wordsMap {
		if key[0] == key[1] && value >= 1 {
			palindromLen += 2
			break
		}
	}

	return palindromLen
}

func main() {
	fmt.Println(longestPalindrome([]string{"lc", "cl", "gg"}))
	fmt.Println(longestPalindrome([]string{"ab", "ty", "yt", "lc", "cl", "ab"}))
	fmt.Println(longestPalindrome([]string{"cc", "ll", "xx"}))
	fmt.Println(longestPalindrome([]string{"qo", "fo", "fq", "qf", "fo", "ff", "qq", "qf", "of", "of", "oo", "of", "of", "qf", "qf", "of"}))
	fmt.Print(longestPalindrome([]string{"bb", "bb"}))
}
