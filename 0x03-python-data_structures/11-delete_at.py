#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deleting an element at index

        Args:
            my_list: List to be traversed

        Returns:
            Returns a new list with deleted index
        """

    if not my_list:
        return None

    new_list = my_list
    list_len = len(my_list)

    if idx < 0 or idx >= list_len:
        return my_list
    del new_list[idx]
    return new_list
