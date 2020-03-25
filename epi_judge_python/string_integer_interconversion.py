import math

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    ans = []
    is_negative = x < 0
    x = abs(x)

    while x >= 0:
        ans.append(chr(ord('0') + x % 10))
        x //= 10

        if x == 0:
            break

    ans = ''.join(reversed(ans))
    return '-' + ans if is_negative else ans


def string_to_int(s: str) -> int:
    ans = 0
    negate = False

    for c in s:
        if c == '-':
            negate = True
            continue
        if c == '+':
            continue
        ans *= 10
        ans += int(c)

    return ans * (-1 if negate else 1)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))