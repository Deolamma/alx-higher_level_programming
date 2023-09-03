#!/usr/bin/python3
"""
This module divides throug a matrix by a divisor
It returns a newlist containing the divided elements to 2dp
For Example: matrix_divided([1, 2, 3], [4, 5, 6], 3) should result in
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Dividing A Matrix By A Divisor

    Args:
        matrix: list of lists containing valid integers OR floats.
                Elements can be either +ve OR -ve.
        div: Div is a valid integer OR float.
             Div can be either +ve OR -ve.

    Return:
        Returns a new matrix(list of lists) containing the divided elements.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 1e-308:
        raise ZeroDivisionError("Number too small to be a divisor")
    standard_len = len(matrix[0])
    for row in matrix:
        if row == []:
            raise TypeError(
                             "matrix must be a matrix (list of lists) "
                             "of integers/floats"
                            )
        if not isinstance(row, list):
            raise TypeError(
                            "matrix must be a matrix (list of lists) "
                            "of integers/floats"
                            )
        elif len(row) != standard_len:
            raise TypeError(
                             "Each row of the matrix must have the same size"
                            )

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                                 "matrix must be a matrix (list of lists) "
                                 "of integers/floats"
                                )
    # Complex list comprehension creating a new matrix(list of lists)
    new_list = [
                    [
                        (round(element / div, 2) if div != 1e308 else 0.0)
                        for element in elements
                    ] for elements in matrix
                ]
    return new_list
