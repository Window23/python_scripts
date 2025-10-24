""" Create a function named calculate_product that receives an arbitrary argument list
    and returns the product of all the arguments. Call the function with the
    arguments 10, 20 and 30, then with the sequence of integers produced by range(1, 6, 2). """

import math



def calculate_product(*prod):
    """ calculate the product of all the arguments. """
    return math.prod(prod)

def calculate_product_2(*args):
    """ calculate the product of all the arguments. """
    product_2 = 1
    for arg in args:
        product_2 *= arg
    return product_2

def calculate_product_3(*args):
    """ calculate the product of all the arguments. """
    product_3 = 1
    for arg in range(1, 6, 2):
        product_3 *= arg
    return product_3

def calculate_product_4(*args):
    """ calculate the product of all the arguments. """
    return math.prod(args)

print(calculate_product(10, 20, 30))
print(calculate_product_2(10, 20, 30))
print(calculate_product_3())
print(calculate_product_4(*range(1, 6, 2)))

