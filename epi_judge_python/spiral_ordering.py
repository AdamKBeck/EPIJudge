from enum import Enum, auto
from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    def traverse_row(row_index, start, end):
        inc = 1 if start < end else -1
        return [square_matrix[row_index][i] for i in range(start, end, inc)]

    def traverse_col(col_index, start, end):
        inc = 1 if start < end else -1
        return [square_matrix[i][col_index] for i in range(start, end, inc)]

    ans = []
    l, r = 0, len(square_matrix)-1

    while l < r:
        ans.extend(traverse_row(l, l, r))
        ans.extend(traverse_col(r, l, r))
        ans.extend(traverse_row(r, r, l))
        ans.extend(traverse_col(l, r, l))

        l += 1
        r -= 1

    if l == r:
        ans.append(square_matrix[l][r])

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
