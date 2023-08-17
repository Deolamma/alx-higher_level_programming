#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
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
