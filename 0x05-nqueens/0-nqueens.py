#!/usr/bin/python3
"""
module doc
"""
from sys import argv


def within_range(queens, new_q):
    x, y = new_q
    for q in queens:
        qx, qy = q
        if (qx == x or qy == y) or (abs(x - qx) == 1 and abs(y - qy) == 1):
            return True
        if abs(qx - x) == abs(qy - y):
            return True

    return False


def nqueens(n):
    solutions = []
    solution = []

    for don in range(n):
        solution.clear()
        solution.append([0, don])

        for x in range(1, n):
            for y in range(n):
                if not within_range(solution, [x, y]):
                    queen = [x, y]
                    solution.append(queen)
        if len(solution) == n:
            solutions.append(solution.copy())
        else:
            solution.clear()

    for s in solutions:
        print(s)
    return solution


if __name__ == "__main__":
    code = 0
    if len(argv) != 2:
        code = 1
        print("Usage: nqueens n")
    else:
        try:
            n = int(argv[1])
        except BaseException:
            print("N must be a number")
    if n < 4:
        code = 1
        print("N must be at least 4")
    else:
        nqueens(n)

    exit(code)
