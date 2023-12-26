#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # computes the square value of all integers of a matrix
    new_matrix = matrix.copy()  # New Matrix

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
        # for each matrix row, a row element is squared

    return new_matrix
