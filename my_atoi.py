class Solution:
    def myAtoi(self, s: str) -> int:
        digits = []
        sign = None
        digits_count = 0
        limit = 2 ** 31

        for char in s:
            if digits_count == 0 and sign is None:
                if char in ["+", "-"]:
                    sign = char
                    continue

                if char == " ":
                    continue

                if not char.isnumeric():
                    break

            if not char.isnumeric() and (digits_count != 0 or sign is not None):
                break

            digit = int(char)
            digits.append(digit)
            digits_count += 1

        number = 0
        for digit in digits:
            number += (digit * (10 ** (digits_count - 1)))
            digits_count -= 1

        if number >= limit:
            number = limit

            if sign is None or sign == "+":
                number -= 1

        if sign == "-":
            number = -1 * number

        return number


def test_1(s_instance: Solution):
    s = "12345"
    number = s_instance.myAtoi(s)
    assert number == 12345, f"{s} != {12345}"


def test_2(s_instance: Solution):
    s = "-12"
    number = s_instance.myAtoi(s)

    assert number == -12


def test_3(s_instance: Solution):
    s = "   42"
    number = s_instance.myAtoi(s)

    assert number == 42


def test_4(solution: Solution):
    s = " -12 aopdjawpodjpwa"

    number = solution.myAtoi(s)

    assert number == -12


if __name__ == '__main__':
    solution_instance = Solution()

    tests = [
        ["12345", 12345],
        ["-12", -12],
        ["   42", 42],
        [" -12 aopdjawpodjpwa", -12],
        ["awojdpoawjdp 42", 0],
        ["-91283472332", -2**31],
        ["91283472332", 2**31 - 1],
        ["+-12", 0],
        ["  +  413", 0]
    ]

    for input_, expected in tests:
        solution = solution_instance.myAtoi(input_)
        assert solution == expected, f"{solution} != {expected}"
