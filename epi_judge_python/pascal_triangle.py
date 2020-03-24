from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n == 0:
        return []

    ans = [[1]]

    for i in range(1, n):
        row = ans[-1]
        new_row = [1]

        for k in range(0, len(row)-1):

            new_row.append(row[k] + row[k+1])

        new_row.append(1)
        ans.append(new_row)

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
