#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    operators = "+-*/"
    if len(sys.argv) != 4:
        sys.exit("Usage: ./100-my_calculator.py <a> <operator> <b>")
    if sys.argv[2] not in operators:
        sys.exit("Unknown operator. Available operators: +, -, * and /")
    a = int(sys.argv[1])
    operator = operators[operators.find(sys.argv[2])]
    b = int(sys.argv[3])
    ans = add(a, b) if operator == "+" else sub(a, b) if operator == "-" \
        else mul(a, b) if operator == "*" else div(a, b)
    print("{} {} {} = {}".format(a, operator, b, ans))


if __name__ == "__main__":
    main()
