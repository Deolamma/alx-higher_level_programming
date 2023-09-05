#!/usr/bin/python
def text_indentation(text):
    new_str = ""
    in_sentence = False
    consecutive_punc = False

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char in [".", "?", ":"]:
            if not consecutive_punc:
                new_str += char + "\n\n"
                in_sentence = False
                consecutive_punc = True
        elif char == " " and in_sentence == False:
            continue;
        else:
            new_str += char
            in_sentence = True
            consecutive_punc =False
    stripped_string = new_str.strip("\r\n")
    print(stripped_string, end="")
