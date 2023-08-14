#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
        Args:
            my_list: List to be copied and replaced at index
            idx: index to replace element in COPIED list
            element: element to be inserted in the COPIED list

        Returns:
            Returns the copied manipulated list or the original list on failure
        """

    list_len = len(my_list) - 1
    new_list = my_list

    if (idx < 0) or (list_len < idx):
        return my_list
    new_list[idx] = element
    return new_list
