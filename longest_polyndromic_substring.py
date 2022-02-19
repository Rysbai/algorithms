from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        l = 0
        r = 0
        window = deque()
        reversed_window = deque()

        longest = []
        longest_len = 0
        current_window_len = 0
        while True:
            if (s_len - l) <= longest_len:
                break

            if r < s_len:
                r_char = s[r]
                window.append(r_char)
                reversed_window.appendleft(r_char)
                current_window_len += 1
                if window == reversed_window and current_window_len > longest_len:
                    longest = window.copy()
                    longest_len = current_window_len
                r += 1
                continue

            l += 1
            r = l
            window = deque()
            reversed_window = deque()
            current_window_len = 0

        return "".join(longest)


if __name__ == '__main__':
    assert Solution().longestPalindrome("babad") == "bab"
    assert Solution().longestPalindrome("cbbd") == "bb"
    assert Solution().longestPalindrome("a") == "a"
    assert Solution().longestPalindrome("ac") == "a"
