#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = [list(map(lambda x: x * x, row)) for row in matrix]
    return a
