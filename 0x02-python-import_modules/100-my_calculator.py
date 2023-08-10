#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv_len = len(sys.argv)
    if argv_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operand = sys.argv[2]
    operators = {"+" : add(a, b),
                 "-" : sub(a, b),
                 "*" : mul(a, b),
                 "/" : div(a, b)}
    for op, fxn in operators.items():
        if (op == operand):
            print("{} {} {} = {}".format(a, op, b, fxn))
            sys.exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

