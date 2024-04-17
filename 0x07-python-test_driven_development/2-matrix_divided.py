#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_lengths = []
        row_lengths.append(len(row))
        if len(set(row_lengths)) != 1:
            raise TypeError("Each row of the matrix must have the same size")
        result = []
        for i in row:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result.append(round(i / div, 2))
        new_matrix.append(result)
    return new_matrix
