#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Safe Printing A Listing

        Args:
            my_list: List to be printed out
            x: number of elements to print out

        Return:
            Returns nothing
    """
    count = 0
    for value in my_list[:x]:
        try:
            int(value)
            print("{:d}".format(value), end="")
            count += 1
        except (ValueError, IndexError):
            pass
    print()
    return count
