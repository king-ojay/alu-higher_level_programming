#!/usr/bin/python3
import sys
from calculator_1 import add, subtract, multiply, divide

def my_calculator():
    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return
    
    # Extract arguments
    try:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return
    
    # Perform the operation based on the operator
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        return
    
    # Print the result
    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    my_calculator()

