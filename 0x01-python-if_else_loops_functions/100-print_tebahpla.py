#!/usr/bin/python3
for ch in range(122, 96, -1):
    print("{}".format(chr(ch) if ((ch % 2) == 0) else chr(ch - 32)), end="")
