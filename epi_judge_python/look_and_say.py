from itertools import groupby
from test_framework import generic_test


def look_and_say(n: int) -> str:
    s = '1'

    for _ in range(1, n):
        ans = ""
        for val, group in groupby(s):
            count = str(len(list(group)))
            ans += count + val
        s = ans

    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
