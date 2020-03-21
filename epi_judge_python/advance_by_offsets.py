from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    end = len(A) - 1
    i = 0
    moves_left = A[i]

    while i + A[i] < end:
        if not moves_left:
            return False

        i += 1
        moves_left = max(moves_left-1, A[i])

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))