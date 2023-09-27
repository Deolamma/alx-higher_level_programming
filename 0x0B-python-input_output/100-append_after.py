#!/usr/bin/python3
"""
This module inserts a line of text after a line containing a certain a text
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserting a Line
    This inserts a line of text after the line containing a certain occurence
    of a string

    Args:
        filename: Name of file to be worked upon
        search_string: This is the text to be found in a certain line
                       if this text is found a given line of text is inserted
                       after the line containing search_string
        new_string: This is the string to be inserted on a new line

    Return:
        NIL
    """
    found_text = False

    with open(filename, "r", encoding="utf-8") as open_read:
        lines = open_read.readlines()

    for i, line in enumerate(lines):
        if search_string in line:
            found_text = True
            lines.insert(i + 1, new_string)

    with open(filename, "w", encoding="utf-8") as open_f:
        if found_text:
            open_f.writelines(lines)
