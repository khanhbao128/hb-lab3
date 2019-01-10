"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    tokens_string = (input (" Please enter operator followed by numbers \n"))
    tokens = tokens_string.split()
    if tokens[0] == 'q':
        break
    if len(tokens) < 2:
        print("We need at least one number")
        continue

    if len(tokens) == 2:
        tokens.append(0)

    if tokens[0] == '+':
        result =  arithmetic.add(int(tokens[1]), int(tokens[2]))
        print(result)
        break

    elif tokens[0] == '-':
        result = arithmetic.subtract(int(tokens[1]), int(tokens[2]))
        print(result)
        break

    elif tokens[0] == '*':
        result = arithmetic.multiply(int(tokens[1]), int(tokens[2]))
        print (result)
        break

    elif tokens[0] == '/':
        result = divide(int(tokens[1]), int(tokens[2]))
        print(result)
        break

    elif tokens[0] == 'square':
        result = square(int(tokens[1]))
        print(result)
        break

    elif tokens[0] == 'cube':
        result = cube(int(tokens[1]))
        print(result)
        break

    elif tokens[0] == 'pow':
        result = power(int(tokens[1]), int(tokens[2]))
        print(result)
        break






