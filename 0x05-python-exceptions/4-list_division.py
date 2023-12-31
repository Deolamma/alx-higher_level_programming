#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Safely Dividing elements of 2 Lists

        Args:
            my_list_1: First list
            my_list_2: Second list
            list_length: Number of elements to divide in the list provided

        Return:
            Returns a new list with result of division
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
