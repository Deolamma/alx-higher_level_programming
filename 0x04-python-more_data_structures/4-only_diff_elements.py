#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    """Different Elements

        Args:
            set_1: First set
            set_2: Second set

        Returns:
            Returns Only elements that occur in set_1 and set_2 but not both
    """

    return set_1 ^ set_2
