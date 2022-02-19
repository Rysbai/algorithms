package main

import "fmt"

var Brackets = map[string]string{
	"(": ")",
	"{": "}",
	"[": "]",
}

var ClosingBrackets = map[string]string{
	")": "(",
	"}": "{",
	"]": "[",
}

func isValid(s string) bool {
	var brackets []string

	for _, char := range s {
		bracket := string(char)

		if _, ok := Brackets[bracket]; ok {
			brackets = append(brackets, bracket)
		} else {
			bracketLen := len(brackets)

			if bracketLen == 0 {
				return false
			}

			var openBracket string

			openBracket, brackets = brackets[bracketLen-1], brackets[:bracketLen-1]
			expectedBracket, _ := ClosingBrackets[bracket]

			if openBracket != expectedBracket {
				return false
			}
		}
	}

	if len(brackets) != 0 {
		return false
	}

	return true
}

func main() {
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(]"))
}
