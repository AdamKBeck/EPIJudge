from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def is_unique(row):
        non_nones = list(filter(lambda x: x != 0, row))  # blank squares = 0
        return len(non_nones) == len(set(non_nones))

    def rows():
        for row in partial_assignment:
            yield row

    def cols():
        for i in range(len(partial_assignment)):
            yield [partial_assignment[j][i] for j in range(len(partial_assignment))]

    def squares():
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                yield [partial_assignment[a][b] for a in range(i, i+3) for b in range(j, j+3)]

    is_valid = lambda xs: all(is_unique(x) for x in xs)
    return is_valid(rows()) and is_valid(cols()) and is_valid(squares())


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))