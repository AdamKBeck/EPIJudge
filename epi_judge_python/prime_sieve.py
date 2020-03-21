from typing import List
from enum import Enum, auto
from math import sqrt

from test_framework import generic_test


class PrimeStatus(Enum):
    UNKNOWN = auto()
    PRIME = auto()
    NOT_PRIME = auto()

    @classmethod
    def is_prime(cls, n):
        if n == 2:
            return cls.PRIME
        if n < 2 or n % 2 == 0:
            return cls.NOT_PRIME

        i = 3
        while i*i <= n:
            if n % i == 0:
                return cls.NOT_PRIME
            i += 2

        return cls.PRIME


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    are_primes = [PrimeStatus.UNKNOWN] * (n+1)

    primes = []

    for i in range(2, n+1):
        if are_primes[i] == PrimeStatus.UNKNOWN:
            are_primes[i] = PrimeStatus.is_prime(i)

            if are_primes[i] == PrimeStatus.NOT_PRIME:
                for k in range(i, n, i):
                    are_primes[k] = PrimeStatus.NOT_PRIME

        if are_primes[i] == PrimeStatus.PRIME:
            primes.append(i)

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))