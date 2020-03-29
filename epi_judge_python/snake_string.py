from test_framework import generic_test


def snake_string(s: str) -> str:
    ans = []

    # top row
    for i in range(1, len(s), 4):
        ans.append(s[i])

    # middle row
    for i in range(0, len(s), 2):
        ans.append(s[i])

    # bottom row
    for i in range(3, len(s), 4):
        ans.append(s[i])

    return ''.join(ans)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
