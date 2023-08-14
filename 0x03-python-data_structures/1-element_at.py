#!/usr/bin/python3
def element_at(my_list, idx):
    """Getting element at certain index of a list
        
        Args:
            my_list: List to retrieve element from
            idx: index to retrieve element at

        Returns:
           Return element at idx or None
        """

    list_len = len(my_list) - 1
    if (idx > list_len) or (idx < 0):
        return None
    return my_list[idx]
