#!/usr/bin/python3
"""
DOC
"""


def primeit():
    # given that n can be <= 10000, we go overboard and prepare a list
    # of primes
    primes = []
    for n in range(1, 10000):
        divided = 0
        for d in range(1, n):
            if n % d == 0:
                divided += 1
            if divided >= 2:
                break
        if divided == 1:
            primes += [n]
    return primes


def isWinner(x, nums):
    """the winner iiiiis..."""

    # +1 for Ben, -1 for Marian, 0 draw
    score = 0
    primes = None
    for r in range(x):
        score_r = 0  # same as @score but per round
        # 1 Ben's turn, 0 Maria's turn
        turn = False
        if nums[r] == 1:
            score += 1
            continue

        # to ensure we call primeit only once
        if primes is None:
            primes = primeit()

        # we extract primal number within nums[r] by intersecting the sets
        round_set = range(nums[r], 0, -1)
        round_set = list(set(primes) & set(round_set))

        for n in round_set:
            if n == 1:
                if turn:
                    score_r -= 1
                else:
                    score_r += 1
                break
            if turn:
                score_r -= 1
            else:
                score_r += 1
            turn = not turn

        if score_r > 0:
            score += 1
        elif score_r < 0:
            score -= 1

    if score == 0:
        return None
    return "Ben" if score > 0 else "Maria"
