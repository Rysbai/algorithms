class Solution:
    def checkString(self, s: str) -> bool:
        is_b = False

        for char in s:
            if char == "a" and is_b:
                return False

            if char == "b":
                is_b = True

        return True


if __name__ == '__main__':
    tests = [
        ["abab", False],
        ["bbb", True],
        ["abab", False]
    ]

    solution_instance = Solution()

    for input_, expected in tests:
        output = solution_instance.checkString(input_)
        assert output == expected, f"{output} != {expected} when input={input_}"

