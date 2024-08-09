#!/usr/bin/python3
"""
DOC
"""


def isPrime(n):
    """
    is n prime num
    """
    primes = 0
    for d in range(1, n):
        if n % d == 0:
            primes += 1
    return primes == 1


def isWinner(x, nums):
    """the winner iiiiis..."""

    # +1 for Ben, -1 for Marian, 0 draw
    score = 0

    for r in range(x):
        score_r = 0  # same as @score but per round
        # 1 Ben's turn, 0 Maria's turn
        turn = False

        if abs(score) > x / 2:
            break
        if nums[r] == 1:
            score += 1
            continue
        for n in range(2, nums[r] + 1):
            if isPrime(n):
                if turn:
                    score_r += 1
                else:
                    score_r -= 1
                turn = not turn
        if score_r > 0:
            score += 1
        elif score < 0:
            score -= 1

    if score == 0:
        return None
    return "Ben" if score > 0 else "Maria"


print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))
