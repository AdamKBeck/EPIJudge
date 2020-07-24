from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    return dp[m-1][n-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))