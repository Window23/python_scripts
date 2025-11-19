""" Intro to Data Science: Survey Response Statistics)
    Twenty students were asked to rate on a scale of 1 to 5 the quality of the food in the student cafeteria, with 1 being “awful” and 5 being “excellent.”
    Place the 20 responses in a list

    1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5

    Determine and display the frequency of each rating.
    Use the built-in functions, statistics module functions and NumPy functions demonstrated in Section 5.17.2
    to display the following response statistics: minimum, maximum, range, mean, median, mode, variance and standard deviation. """


import random
import statistics
import numpy



lst = [random.randint(1, 5) for i in range(20)]

printing = []

for item in lst:
    items = (item, lst.count(item))
    printing.append(items)
print(lst)
printing = list(set(printing))
print("min = ",  min(lst))
print("max = ",  max(lst))
print("range = ", min(lst), '-', max(lst))
print("mean = ", statistics.mean(lst))
print("median = ", statistics.median(lst))
print("mode = ", statistics.mode(lst))
print("variance = ", numpy.var(lst))
print("standard_deviation = ", numpy.std(lst))


print(list(set(printing)))

for item, occurrences in printing:
    print(f"We found the item {item} with {occurrences} occurrences.")
