class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        string_length = len(s)
        left_p = 0
        right_p = 0
        window = []
        dubbed_char = ""

        while True:
            if longest >= (string_length - right_p) or left_p >= string_length:
                break

            if not dubbed_char or not window:
                char = s[left_p]
                if char in window:
                    dubbed_char = char
                else:
                    longest = max(len(window) + 1, longest)
                window.append(char)
                left_p += 1
                continue

            char = window.pop(0)
            right_p += 1
            if char == dubbed_char:
                dubbed_char = ""

        return longest