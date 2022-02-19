from typing import List


class Solution:

    def find_next_optimal_step(self, current_i, max_step, nums):
        max_num = 0
        next_step = 1

        for i in range(1, max_step + 1):
            num = nums[current_i + i]

            if num + i >= max_num:
                max_num = num + i
                next_step = i

        return next_step

    def jump(self, nums: List[int]) -> int:
        steps = 0
        current_i = 0
        nums_len = len(nums)

        if nums_len == 1:
            return 0

        while current_i < nums_len:
            max_step = nums[current_i]
            if current_i + (max_step + 1) >= nums_len:
                steps += 1
                break

            next_step = self.find_next_optimal_step(current_i, max_step, nums)
            current_i += next_step
            steps += 1

        return steps


if __name__ == '__main__':
    tests = [
        [[2, 3, 1, 1, 4], 2],
        [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0], 2]
    ]

    solution_instance = Solution()

    for input_, expected in tests:
        output = solution_instance.jump(input_)
        assert output == expected, f"{output} != {expected} when input={input_}"
