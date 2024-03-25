#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixA = []
    for i in matrix:
        squared_row = []
        for element in i:
            squared_row.append(element ** 2)
        matrixA.append(squared_row)
    return matrixA
    # x = []
    # for i in matrix:
    # x.append(list(map(lambda x : x ** 2, i)))
    # return(x)
