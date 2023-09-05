#!/usr/bin/python3
"""
This module indents a text by replacing the characters ".", "?", and ":"
with two blank lines
For Example:
    "My name. is: Emmanuel..."
Should print:
    My name.

    is:

    Emmanuel...
"""


def text_indentation(text):
    """
    Text Indentation Of Strings
    This module replaces a ".", "?", and ":" with "\n\n"

    Args:
        text: This is the text to be indented

    Return:
        Nothing. Prints the new indented text
    """

    new_str = ""
    in_sentence = False
    consecutive_punc = False

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for index, char in enumerate(text):
        if char in [".", "?", ":"]:

            # this checks that consecutive_punc is FALSE so:
            # not consecutive_punc == TRUE, evaluates (if true)
            if not consecutive_punc:
                # I check if the next char is a ".", ":", "?"
                if (
                        (index + 1 < len(text)) and
                        (text[index + 1] in [".", "?", ":"])):
                    new_str += char
                    in_sentence = False
                    consecutive_punc = False
                else:
                    new_str += char + "\n\n"
                    in_sentence = False
                    consecutive_punc = True
        elif char == " " and in_sentence is False:
            continue
        else:
            new_str += char
            in_sentence = True
            consecutive_punc = False
    stripped_string = new_str.strip("\r\n")
    print(stripped_string, end="")
