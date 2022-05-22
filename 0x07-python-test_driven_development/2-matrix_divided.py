#!/usr/bin/python3
"""Divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix

    Args:
        matrix: list of list of int or floats
        div: number that elements of matrix should be divided

    Raises:
        raise TypeError if matrix is not a list of list of int or floats
        raise TypeError if rows have not the same size
        raise TypeError if div is not a number
        raise ZeroDivisionError if div is equal to 0
    """
    newmatrix = []
    for rows in matrix:
        if type(matrix) != int or type(matrix) != float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(rows) != len(rows):
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) != int or type(div)!= float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        result = rows / div
    newmatrix.append(result)
    return newmatrix
