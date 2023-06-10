#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) <= 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        Total = 0
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == "+":
            Total = add(a, b)
            print("{} {} {} = {}".format(a, operator, b, Total))
        elif operator == "-":
            Total = sub(a, b)
            print("{} {} {} = {}".format(a, operator, b, Total))
        elif operator == "*":
            Total = mul(a, b)
            print("{} {} {} = {}".format(a, operator, b, Total))
        elif operator == "/":
            Total = div(a, b)
            print("{} {} {} = {}".format(a, operator, b, Total))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
