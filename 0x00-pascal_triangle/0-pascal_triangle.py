#!/usr/bin/python3
""" pascal_triangle """

def pascal_triangle(n):
    """ pascal_triangle """
    pascal = []
    if n <= 0:
        return pascal
    
    for row in range(1,n+1):
        i = []
        for col in range(1,row+1):
            if col == 1:
                i += [1]
            else:
                try:
                    i += [ pascal[row-2][col-1]+pascal[row-2][col-2] ]
                except:
                    i += [1]
        pascal += [i]
    return pascal

if __name__ == "__main__":
    pascal_triangle(0)
