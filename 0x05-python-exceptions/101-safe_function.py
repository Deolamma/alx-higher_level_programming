#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executing a function safely

        Args:
            fct: function to be executed safely
            args: variable number of positional arguments

        Return:
            Returns result of the execution of the function OR None
    """
    try:
        result = fct(*args)
    except Exception as e:
        result = None
        print(f"Exception: {e}", file=sys.stderr)
    finally:
        return result
