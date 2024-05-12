#!/usr/bin/python3
""" MinOps """
import math


def clear_list(list: list, base: int) -> list:
    """
    @new_list the new list which will contain factors
                that are divisible by @base
    @appended is used to ignore the next two factors
                that are divisible by @base to reduce 
                number of ops required to reach @n
    """
    new_list = []
    appended = 0
    for i in list:
        if i % base == 0:
            if appended == 0:
                appended = 2
                new_list.append(i)
            else:
                appended -= 1
    return new_list


def getPrimeN(n: int) -> list:
    """
        Return the smallest factor number @p
        if @n has no factor return @n
    """
    primes = []
    for p in range(3, n):
        if n % p == 0:
            primes.append(p)
    return primes if len(primes) > 0 else [n]


def minOperations(n: int) -> int:
    """
        @n number of copies of desired character
        @base is the factor which we will keep adding
            to @chars to reach @n
        @ops number of operations done
    """
    base_list = getPrimeN(n)
    base = base_list.pop(0)
    base_list = clear_list(base_list, base)

    if n <= 1 or math.isinf(n):
        return 0
    elif base == n:
        return n

    ops = base
    chars = base

    while chars != n:
        ops += 1
        chars += base
        if len(base_list) >= 1:
            if base_list[0] < chars:
                base_list.pop(0)
            elif base_list[0] == chars:
                ops += 1
                base = base_list.pop(0)

    if chars == base:
        return ops

    return ops + 1
