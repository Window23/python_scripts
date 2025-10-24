""" Requirements statement:
    Use a for statement, randrange and a conditional expression (introduced in the preceding chapter)
    to simulate 20 coin flips, displaying H for heads and T for tails all on the same line, each separated by a space. """

import random

def heads_tails():
    result = []
    for _ in range(20):
        roll = random.randrange(0, 2)
        if roll == 0:
            result.append("H")
        elif roll == 1:
            result.append("T")
    return print(result)

def heads_tails_2():
    for _ in range(20):
        print('H' if random.randrange(2) == 0 else 'T', end=' ')
    return print()

heads_tails()
heads_tails_2()

