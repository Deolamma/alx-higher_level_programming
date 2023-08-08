#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{0}".format(c if ((ord(c) >= 65) and (ord(c) <= 90)
              or c.isdigit() or c == " ") else (chr(ord(c) - 32))), end="")
    print("{}".format(""))
