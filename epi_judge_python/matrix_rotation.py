from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    def rotate(i, j):
        A = square_matrix

        A[i][j], A[j][-1-i], A[-1-i][-1-j], A[-1-j][i] = (
            A[-1-j][i], A[i][j], A[j][-1-i], A[-1-i][-1-j]
        )

    for i in range(len(square_matrix)//2):
        for j in range(i, len(square_matrix)-1-i):
            rotate(i, j)


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))