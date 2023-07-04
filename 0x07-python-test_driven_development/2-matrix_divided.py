#!/usr/bin/python3
"""
    Defines a function matrix_divided(matrix, div) that divides
    all elements in matrix with div.
"""

def matrix_divided(matrix, div):
    """
        Args:
            matrix: Contains integers/floats elements.
            div: An integer used to divide all the elements in matrix
        Returns:
            A new matrix
    """
    outer_matrix = []
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])

    for i in range(0, len(matrix)):
        if len(matrix[i]) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        inner_matrix = []
        for element in lists:
            if len(lists) == 0:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            inner_matrix.append(round((element / div), 2))
        outer_matrix.append(inner_matrix)

    return (outer_matrix)
