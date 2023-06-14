#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = [[x*x for x in row] for row in matrix]
    return a
