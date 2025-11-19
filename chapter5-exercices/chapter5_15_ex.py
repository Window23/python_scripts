""" (Sorting Letters and Removing Duplicates) letter. Perform the following tasks and display your results:

    1.Sort the list in ascending order.
    2.Sort the list in descending order.
    3.Get the unique values sort them in ascending order. """

import random

def sort_letters_ascending(arg):
    return sorted(arg)

def sort_letters_descending(arg):
    return sorted(arg, reverse=True)

def sort_letters_set(arg):
    return sorted(set(arg))

letters = [chr(random.randrange(ord('a'), ord('f') +1)) for _ in range(20)]

print(sort_letters_ascending(letters))
print(sort_letters_descending(letters))
print(sort_letters_set(letters))


