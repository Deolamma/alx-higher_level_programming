#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Printing elments of a list in list
        Args:
            matrix: List in List

        Returns:
            Returns nothing.
    """

    for i, elements in enumerate(matrix):
        for j, element in enumerate(elements):
            print("{:d}".format(element), end=" ")
        print()
