#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replacing all occurences of an element in list

        Args:
            my_list: List to be traversed
            search: element to be replaced
            replace: new element

        Returns:
            Returns a new list with replaced element at index
    """

    new_list = [replace if element == search else element
                for element in my_list]

    return new_list
