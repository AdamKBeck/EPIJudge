from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    if not s:
        return 0

    for i, x in enumerate(t):
        if x == s[0] and t[i:i+len(s)] == s:
            return i

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
