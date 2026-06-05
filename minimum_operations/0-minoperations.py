#!/usr/bin/python3
"""Compute the fewest Copy-All/Paste operations to reach n characters."""


def minOperations(n):
    """Return the minimum number of operations needed to reach n H's.

    The editor starts with a single H and supports only Copy-All and
    Paste. Reaching n characters takes the sum of n's prime factors
    operations; for n <= 1 the target is unreachable.
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
