from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    i = len(A) - 1

    while i >= 0:
        if A[i] == 9:
            A[i] = 0
        else:
            A[i] += 1
            return A

        i -= 1

    # Instead of ```return [1] + A```, we do this to save runtime
    A[0] = 1
    A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))