#!/usr/bin/python3
def best_score(a_dictionary):

    """Returning key with highest score

        Args:
            a_dictionary: Dictionary to be traversed

        Returns:
            Returns the key with the highest value
    """

    if a_dictionary is None or not a_dictionary:
        return None

    best_score = 0
    best_score_key = ""

    for k, v in a_dictionary.items():
        if a_dictionary[k] > best_score:
            best_score = a_dictionary[k]
            best_score_key = k
    return best_score_key
