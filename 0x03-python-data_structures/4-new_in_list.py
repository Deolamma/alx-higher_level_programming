#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replacing data in a copy of a list
        Args:
            my_list: List to be copied
            idx: index to be accessed in the copied list
            element: data to be inserted at index of copied list

        Returns:
            Returns altered copied list
        """

    list_len = len(my_list) - 1
    new_list = my_list.copy()
    if (idx > list_len) or (idx < 0):
        return my_list
    new_list[idx] = element
    return new_list
