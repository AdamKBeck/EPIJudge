from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # 1. Go from reverse, find the first element where all elements after it are decreasing
    def index_to_swap():
        for i in range(len(perm)-1, 0, -1):
            if perm[i-1] < perm[i]:
                return i-1
        return None

    i = index_to_swap()
    if i is None:
        return []  # default value when perm is already at its max

    # 2. swap i with the next highest element
    for j in reversed(range(i+1, len(perm))):
        if perm[j] > perm[i]:
            perm[i], perm[j] = perm[j], perm[i]
            break

    # 3. reverse the rest of the list [i+1...n]
    perm[i+1:] = reversed(perm[i+1:])

    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))