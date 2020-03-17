from math import pow
from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False

    copy = x
    result = 0

    while x:
        result *= 10
        result += x % 10
        x //= 10

    return result == copy



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))