#!/usr/bin/python3
"""
0-main
"""


def island_perimeter(grid):
    """Doc
    """
    perim = 0
    MAX_X, MAX_Y = len(grid[0]), len(grid)

    for Y in range(0, MAX_Y):
        for X in range(0, MAX_X):
            x1 = X + 1
            y1 = Y + 1
            if grid[Y][X] == 1:
                if (X == 0 or X == MAX_X - 1) and (Y == 0 or Y == MAX_Y - 1):
                    perim += 2
                elif X == 0 or Y == 0 or X == MAX_X-1 or Y == MAX_Y - 1:
                    perim += 1
            if (x1 < MAX_X):
                if (grid[Y][x1] != grid[Y][X]):
                    perim += 1
            if (y1 < MAX_Y):
                if (grid[y1][X] != grid[Y][X]):
                    perim += 1
    return perim
