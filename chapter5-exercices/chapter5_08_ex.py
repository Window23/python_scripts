""" sorting a list """

import random as rnd


def sort_list_a(args):
    args.sort(reverse=True)
    return args

numbers = [rnd.randrange(100) for x in range(10)]
print(sort_list_a(numbers))

