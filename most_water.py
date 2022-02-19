from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        length = len(height)
        l_pointer = 0
        r_pointer = length - 1

        while True:
            if l_pointer == r_pointer:
                break

            l_line = height[l_pointer]
            r_line = height[r_pointer]

            x_value = r_pointer - l_pointer
            y_value = min(r_line, l_line)

            max_area = max(max_area, x_value * y_value)

            if l_line < r_line:
                l_pointer += 1
            else:
                r_pointer -= 1

        return max_area


if __name__ == '__main__':
    tests = [
        [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
        [[1, 1], 1],
        [[2, 1], 1],
        [[1, 8, 6, 2, 5, 4, 8, 25, 7], 49],
        [[8, 20, 1, 2, 3, 4, 5, 6], 42]
    ]
    solution_instance = Solution()

    for input_, expected in tests:
        output = solution_instance.maxArea(input_)

        assert output == expected, f"{output} != {expected} when input={input_}"
