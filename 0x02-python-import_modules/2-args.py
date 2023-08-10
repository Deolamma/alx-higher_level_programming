#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    argv_len -= 1
    print("{} {}".format((argv_len), "argument" if (argv_len == 1)
                         else "arguments"), end="")
    print("{}".format("." if (argv_len == 0) else ":"))
    if argv_len != 0:
        for i, elem in enumerate(sys.argv):
            if i == 0:
                continue
            print("{}: {}".format(i, elem))
