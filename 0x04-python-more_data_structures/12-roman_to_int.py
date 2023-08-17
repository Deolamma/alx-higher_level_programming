#!/usr/bin/python3
def roman_to_int(roman_string):

    """Converting Roman Numeral To Integer

    Args:
        roman_string: Roman numeral to be converted to int

    Returns:
        Returns the corresponding value as integer
    """

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    key_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    total = 0

    for numerals in reversed(roman_string):
        value = key_numerals[numerals]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
    return total
