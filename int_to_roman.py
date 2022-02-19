translator = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        str_num = str(num)
        length = len(str_num)

        for i, digit in enumerate(str_num):
            digit = int(digit)
            rank = 10**(length - i - 1)

            if digit < 4:
                roman_digit = translator[rank]
                roman += (roman_digit * digit)
                continue

            prev_rank = rank
            rank = rank * 5

            if digit in [4, 9]:
                if digit == 9:
                    prev_rank = 10**(length - i - 1)
                    rank = rank * 2
                prev_raman_digit = translator[prev_rank]
                next_roman_digit = translator[rank]
                roman += (prev_raman_digit + next_roman_digit)
                continue

            # if 5 <= digit < 9
            roman_digit = translator[rank]
            prev_raman_digit = translator[prev_rank]
            roman += (roman_digit + (prev_raman_digit * (digit - 5)))

        return roman


if __name__ == '__main__':
    tests = [
        [58, "LVIII"],
        [3, "III"],
        [1994, "MCMXCIV"],
    ]
    solution_instance = Solution()

    for input_, expected in tests:
        output = solution_instance.intToRoman(input_)
        assert output == expected, f"{output} != {expected} when input={input_}"
