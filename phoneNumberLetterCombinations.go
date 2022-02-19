package main

import (
	"fmt"
	"strconv"
)

var PhoneLetters = map[int][4]string{
	2: {"a", "b", "c"},
	3: {"d", "e", "f"},
	4: {"g", "h", "i"},
	5: {"j", "k", "l"},
	6: {"m", "n", "o"},
	7: {"p", "q", "r", "s"},
	8: {"t", "u", "v"},
	9: {"w", "x", "y", "z"},
}

func pullCombinations(comb string, restDigits string) []string {
	restDigitsLen := len(restDigits)

	if restDigitsLen == 0 {
		return []string{}
	}

	digit, _ := strconv.Atoi(string(restDigits[0]))
	letters := PhoneLetters[digit]

	var combinations = []string{}

	for _, letter := range letters {
		if letter == "" {
			continue
		}

		newComb := comb + letter

		if restDigitsLen == 1 {
			combinations = append(combinations, newComb)
			continue
		}

		newCombos := pullCombinations(newComb, string(restDigits[1:]))
		combinations = append(combinations, newCombos...)
	}

	return combinations
}

func letterCombinations(digits string) []string {
	return pullCombinations("", digits)
}

func main() {
	fmt.Println(letterCombinations("23"))
}
