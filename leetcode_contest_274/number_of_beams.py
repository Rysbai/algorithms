from typing import List


class Solution:
    def get_device_count(self, row: str) -> int:
        count = 0
        for char in row:
            if char == "1":
                count += 1

        return count

    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0

        prev_count = self.get_device_count(bank[0])
        for row in bank[1:]:
            device_count = self.get_device_count(row)
            if device_count == 0:
                continue
            beams += (device_count * prev_count)
            prev_count = device_count

        return beams


if __name__ == '__main__':
    tests = [
        [["000", "111", "000"], 0],
        [["011001", "000000", "010100", "001000"], 8],
    ]

    solution_instance = Solution()

    for input_, expected in tests:
        output = solution_instance.numberOfBeams(input_)
        assert output == expected, f"{output} != {expected} when input={input_}"
