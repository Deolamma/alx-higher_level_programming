#!/usr/bin/python3
"""
A class that inherits from the built in list class
"""


class MyList(list):
    """
        A class that inherits from the builtin list class
    """

    def __init__(self):
        """
            constructor of the MyList class
            it calls the init method of the superclass
        """

        super().__init__()

    def print_sorted(self):
        """
        Prints a sorted list in ascending order
        """

        sort_list = sorted(self)
        print(sort_list)
