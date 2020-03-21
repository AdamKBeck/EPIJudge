from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    def calc_best_forwards():
        best_forwards = [0] * len(prices)
        best = 0
        min_stock = prices[0]

        for i, x in enumerate(prices):
            min_stock = min(min_stock, x)
            best = max(best, x - min_stock)
            best_forwards[i] = best

        return best_forwards

    best_forwards = calc_best_forwards()
    best_profit = best_forwards[-1]

    # go in reverse
    max_stock = prices[-1]
    for i in range(len(prices)-1, 0, -1): # intentionally don't look at the 0-th element
        x = prices[i]
        max_stock = max(max_stock, x)
        best_profit = max(best_profit, max_stock - x + best_forwards[i-1])

    return best_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
