#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Printing Valid integers in a List

        Args:
            my_list: List to be treversed
            x: number of elements to be printed out

        Return:
            returns the number of valid integer printed
    """
    count, list_len = 0, 0

    for i in range(x):
        try:
            int(my_list[i])
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, OverflowError, TypeError):
            pass
        except IndexError:
            raise
    print()
    return count
