#!/usr/bin/python3
"""
0-main
"""


def island_border(grid, x, y, borders):
    if grid[y][x] == 0:
        borders.append({'x': x, 'y': y})
        return 1
    return 0


def island_perimeter(grid):
    """Doc
    """
    perim = 0

    # stores the coords of each border as {x,y}, to avoid counting it more
    # than once .
    borders = []

    # grid[y][x]
    MAX_X, MAX_Y = len(grid[0]), len(grid)

    for Y in range(0, MAX_Y):
        for X in range(0, MAX_X):
            if grid[Y][X] == 1:
                x, y = X, Y

                x = [x, x + 1, x - 1]
                y = [y, y + 1, y - 1]

                for _x in x:
                    if _x >= MAX_X:
                        #beyond the grid lies water
                        perim += 1
                        continue
                    elif _x < 0:
                        perim += 1
                        continue
                    perim += island_border(grid, _x, y[0], borders)
                for _y in y:
                    if _y >= MAX_Y:
                        perim += 1
                        continue
                    elif _y < 0:
                        perim += 1
                        continue
                    perim += island_border(grid, x[0], _y, borders)

    return perim
