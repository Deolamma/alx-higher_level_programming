#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Printing the squares of a list

        Args:
            matrix: List in lists

        Return:
            Returns a new list containing the squares of each element
    """

    new_list = [[(element ** 2) for element in elements]
                for elements in matrix]

    return new_list
