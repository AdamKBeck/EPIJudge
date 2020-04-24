from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    stack = []

    for i, x in enumerate(sequence):
        while stack and stack[-1][1] <= x:
            stack.pop()

        stack.append([i, x])

    return [x[0] for x in reversed(stack)]



def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
