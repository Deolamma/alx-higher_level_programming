#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Printing elments of a list in list
        Args:
            matrix: List in List

        Returns:
            Returns nothing.
    """

    for elements in matrix:
        for i, element in enumerate(elements):
            elem_len = len(elements)
            print("{:d}".format(element),
                  end=" " if (i < (elem_len - 1)) else "")
        print()
