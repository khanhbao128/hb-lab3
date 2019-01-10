"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    
    sum = num1 + num2

    return int(sum)


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    d = num1 - num2

    return int(d)



def multiply(num1, num2):
    """Multiply the two inputs together."""
    mul = num1 * num2
    return (int(mul))


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    div = num1 / num2
    return div


def square(num1):
    """Return the square of the input."""
    squr = num1 ** 2
    return(squr)

def cube(num1):
    """Return the cube of the input."""
    cubed = num1 ** 3
    return cubed


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    pw= num1 ** num2
    return pw


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    m = num1 % num2
    return m
