import heapq

from typing import List
from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # push the first elements of each array into the heap
    seen = []

    for i, arr in enumerate(sorted_arrays):
        if arr:
            heapq.heappush(seen, (arr[0], i))

    ans = []
    indices = [0] * len(sorted_arrays)

    while seen:
        next_elem = heapq.heappop(seen)
        i = next_elem[1]
        ans.append(next_elem[0])

        if indices[i] + 1 < len(sorted_arrays[i]):
            indices[i] += 1
            heapq.heappush(seen, (sorted_arrays[i][indices[i]], i))

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
