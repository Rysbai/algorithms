def fib_v1(n: int) -> int:
    if n <= 2:
        return 1

    return fib_v1(n - 1) + fib_v1(n - 2)


# Fibonachi implementation v2 with "memoization"

def fib_v2(n: int, pre_calc: dict = {}) -> int:
    if n <= 2:
        return 1

    if n in pre_calc:
        return pre_calc[n]

    pre_calc[n] = fib_v2(n - 1, pre_calc) + fib_v2(n - 2, pre_calc)
    return pre_calc[n]


if __name__ == "__main__":
    print(fib_v1(6))
    print(fib_v2(100))


