""" (Arbitrary Argument List)
    Calculate the product of a series of integers that are passed to the function product, which receives an arbitrary argument list.
    Test your function with several calls, each with a different number of arguments. """
import random

len_numbers = len(range(random.randrange(1,101)))



a = []

for x in range(len_numbers):
    a.append(random.randrange(random.randrange(1,101)))

def product_of_numbers(*args):
    product = 1
    for i in args:
        product *= i
    return print(f'List of numbers = {args}\nThe product of these numbers is {product}')

product_of_numbers(*a)

