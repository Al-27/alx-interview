#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """mkCH
    """
    if total <= 0:
        return 0
    # eg: if @total is odd and @coins contains no odd number then
    # it's unsolvable
    if total % 2 not in [e % 2 for e in coins] or len(coins) == 0:
        return -1
    coins.sort(reverse=True)
    coins_req = 0
    i = 0
    while (total != 0):
        if i >= len(coins):
            break
        coin = coins[i]
        if total < coin:
            i += 1
            continue

        total = total - coin
        coins_req += 1
    if coins_req == 0 or total != 0:
        return -1
    return coins_req
