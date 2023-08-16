#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    """Printing Sorted Dictionary

        Args:
            a_dictionary: Dictionary to be sorted

        Returns:
            Prints a sorted dictionary line by line
    """

    for element in sorted(a_dictionary):
        print("{}: {}".format(element, a_dictionary[element]))
