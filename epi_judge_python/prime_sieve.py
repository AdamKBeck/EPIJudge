from typing import List
from enum import Enum, auto
from math import sqrt

from test_framework import generic_test


class PrimeStatus(Enum):
    PRIME = auto()
    NOT_PRIME = auto()


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    are_primes = [PrimeStatus.NOT_PRIME, PrimeStatus.NOT_PRIME] + [PrimeStatus.PRIME] * n
    primes = []

    for i in range(2, n+1):
        if are_primes[i] == PrimeStatus.PRIME:
            primes.append(i)

            for k in range(i, n+1, i):
                are_primes[k] = PrimeStatus.NOT_PRIME

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))