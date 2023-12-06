#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = [[value ** 2 for value in row] for row in matrix]
    return sqr
