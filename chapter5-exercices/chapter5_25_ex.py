""" Intro to Data Science: Duplicate Elimination and Counting Frequencies)
    Use a list comprehension to create a list of 50 random values in the range 1 through 10.
    Use NumPy’s unique function to obtain the unique values and their frequencies. Display the results. """

import random
import numpy

list_compre = [random.randint(1, 10) for _ in range(50)]
print(numpy.unique_counts(list_compre))