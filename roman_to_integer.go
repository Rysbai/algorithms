package main

import "fmt"

var Translators = map[string]int{
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000,
}

func romanToInt(s string) int {
	sLen := len(s)
	sRun := []rune(s)
	pos := 0

	number := 0
	for pos < sLen {
		char := string(sRun[pos])
		var nextChar string
		if pos < sLen-1 {
			nextChar = string(sRun[pos+1])
		}

		val := Translators[char]
		nextVal := Translators[nextChar]

		if val < nextVal {
			number += nextVal - val
			pos += 2
			continue
		}

		number += val
		pos++
	}

	return number
}

func main() {
	fmt.Println(romanToInt("MCMXCIV"))
}
