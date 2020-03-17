from test_framework import generic_test


def reverse(x: int) -> int:
    result = 0
    positive_x = abs(x)

    while positive_x:
        result = result * 10 + positive_x % 10
        positive_x //= 10

    return -result if x < 0 else result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
