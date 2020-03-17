import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    def zero_to_x_random(x):
        """
        Find a random number between [0,y], where x = upper_bound - lower_bound,
        and y = the greatest number you can form from the amount of bits that x is.
        """
        solution = 0

        while x != 0:
            x >>= 1
            solution *= 2
            solution += zero_one_random()

        return solution

    x = upper_bound - lower_bound
    ans = zero_to_x_random(x) + lower_bound

    while ans > upper_bound:
        ans = zero_to_x_random(x) + lower_bound

    return ans


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
