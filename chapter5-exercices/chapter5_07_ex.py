""" Create a list called numbers containing the values from 1 through 15, then use the del statement to perform the following operations consecutively:
    Delete a slice containing the first four elements, then show the resulting list.
    Starting with the first element, use a slice to delete every other element of the list, then show the resulting list. """

numbers = list(range(1, 16))

del numbers[:4]
print(numbers)


del numbers[::2]
print(numbers)



