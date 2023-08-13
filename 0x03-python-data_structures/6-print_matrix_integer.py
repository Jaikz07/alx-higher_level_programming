#!/usr/bin/python3

# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""

    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" " if col != row[-1] else "")
            print()
