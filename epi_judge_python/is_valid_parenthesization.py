from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    open_to_close = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    stack = []

    for x in s:
        if x in open_to_close:
            stack.append(x)
        elif not stack:
            return False
        else:
            opening = stack.pop()
            if open_to_close[opening] != x:
                return False

    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
