#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """"
y   =  1 2 3
       . . .
y-n =  7 8 9 -- we start from here
then:
        7 . 1
        8 . 2
        9 . 3
    """
    result = []
    for y in range(len(matrix)-1,-1,-1):
        for x in range(len(matrix)):
            if len(result) < len(matrix):
                result.append([matrix[y][x]])
            else:
                result[x].append(matrix[y][x])
    matrix[:] = result
