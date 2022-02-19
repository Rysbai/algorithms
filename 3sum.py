from typing import List


class Solution:
    def find_num(self, search_num: int, sorted_nums, nums_len, exclude_i, exclude_j) -> int:
        get_next_i = lambda x: x + 1
        can_stop = lambda num: num > search_num
        i = 0

        if search_num >= 0:
            get_next_i = lambda x: x - 1
            can_stop = lambda num: num < search_num
            i = nums_len - 1

        while True:
            num_index, num = sorted_nums[i]
            if num == search_num:
                if num_index != exclude_i and num_index != exclude_j:
                    return num

            i = get_next_i(i)
            if i >= nums_len or i < 0:
                break

            if can_stop(num):
                break

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        enumerated_nums = enumerate(nums)
        sorted_nums = sorted(enumerated_nums, key=lambda x: x[1])
        triplets = {}

        for i in range(nums_len):
            i_num = nums[i]
            for j in range(nums_len):
                if i == j:
                    continue
                j_num = nums[j]

                half_sum = i_num + j_num
                k_num = -half_sum
                triple = [i_num, j_num, k_num]
                key = frozenset(triple)
                if key in triplets:
                    continue

                k_num = self.find_num(k_num, sorted_nums, nums_len, i, j)
                if k_num is not None:
                    triplets[key] = triple

        return triplets.values()


if __name__ == '__main__':
    tests = [
        [[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]],
        [[0, 0], []],
        [[0, 0, 0], [[0, 0, 0]]],
        [[0, 1, -1], [[0, 1, -1]]]
    ]

    solution_instance = Solution()

    for input_, expected in tests:
        output = solution_instance.threeSum(input_)
        print(f"{list(output)} == {expected}")
