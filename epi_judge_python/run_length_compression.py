from itertools import groupby

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    ans = []
    i = j = 0

    while j < len(s):
        if not s[j].isalpha():
            j += 1
        else:
            ans.append(int(s[i:j]) * s[j])
            j += 1
            i = j

    return ''.join(ans)


def encoding(s: str) -> str:
    ans = []

    for letter, group in groupby(s):
        ans.append(str(len(list(group))))
        ans.append(letter)

    return ''.join(ans)



def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))