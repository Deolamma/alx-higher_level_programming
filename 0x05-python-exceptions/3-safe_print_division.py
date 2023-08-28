#!usr/bin/python3
def safe_print_division(a, b):
    """Dividing Safely

        Args:
            a: first integer
            b: second integer

        Return:
            Returns the result of the division OR None if it fails
    """
    try:
        int(a)
        int(b)
        result = a / b
    except (FloatingPointError, ZeroDivisionError, TypeError, ValueError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
