from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)

        for asteroid in asteroids:
            if mass < asteroid:
                return False

            mass += asteroid

        return True


if __name__ == '__main__':
    tests = [
        [[10, [3, 9, 19, 5, 21]], True],
        [[5, [4, 9, 23, 4]], False],
    ]

    solution_instance = Solution()

    for input_, expected in tests:
        output = solution_instance.asteroidsDestroyed(*input_)
        assert output == expected, f"{output} != {expected} when input={input_}"
