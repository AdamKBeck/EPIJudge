from test_framework import generic_test


ROMAN_TO_INT = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_integer(s: str) -> int:
    acc = 0

    for i, x in enumerate(s):
        if i+1 < len(s) and ROMAN_TO_INT[x] < ROMAN_TO_INT[s[i+1]]:
            acc += -ROMAN_TO_INT[x]
        else:
            acc += ROMAN_TO_INT[x]

    return acc


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
