""" Create the list names containing three name strings.
    Use a for loop and the enumerate function to iterate through the elements and display each element’s index and value. """

names = ('Marian', 'John', 'Vladimir', 'Emilian')

for index, name in enumerate(names):
    print(f'{index:>2} {name}')