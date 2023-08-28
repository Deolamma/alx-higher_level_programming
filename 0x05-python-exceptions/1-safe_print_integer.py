#!/usr/bin/python3
def safe_print_integer(value):
    """Printing a valid integer value

        Args:
            value: value to be printed out

        Return:
            Returns True if value is a valid integer
    """
    try:
        int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
