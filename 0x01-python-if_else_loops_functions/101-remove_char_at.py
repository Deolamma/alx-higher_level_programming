#!/usr/bin/python3
def remove_char_at(str, n):

    i = 0
    new_str = ""
    for i, ch in enumerate(str):
        if i == n:
            continue
        new_str += str[i]
    return new_str
