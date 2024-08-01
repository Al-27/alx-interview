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
            if (x1 < MAX_X):
                if (grid[Y][x1] != grid[Y][X]):
                    perim += 1
            if (y1 < MAX_Y):
                if (grid[y1][X] != grid[Y][X]):
                    perim += 1
    return perim
