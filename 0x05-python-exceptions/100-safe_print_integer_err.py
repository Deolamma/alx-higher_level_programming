#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Printing a valid integer value

        Args:
            value: value to be printed out

        Return:
            Returns True if value is a valid integer
            Returns False if value is not valide and prints to STDERR
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, OverflowError, TypeError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
