#!/usr/bin/python3
""" MinOps """
import math


def getPrimeN(n: int) -> list:
    """
        Return the smallest prime number @p
        if @n has no prime divider return @n
    """
    primes = []
    for p in range(3, n):
        if n % p == 0:
            primes.append(p)
    return primes[0] if len(primes) > 0 else n


def minOperations(n: int) -> int:
    """
        @n number of copies of desired character
        @base is the prime number with which we will keep adding
            to @chars to reach @n
        @ops number of operations done
    """
    base = getPrimeN(n)

    if n <= 1 or math.isinf(n):
        return 0
    elif base == n:
        return n

    ops = base
    chars = base

    while chars != n:
        ops += 1
        chars += base

    if chars == base:
        return ops

    return ops + 1
