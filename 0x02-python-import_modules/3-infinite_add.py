#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    sum = 0
    if argv_len == 0:
        print("0")
    for i, elem in enumerate(sys.argv):
        if i == 0:
            continue
        sum += int(elem)
    print(sum)
