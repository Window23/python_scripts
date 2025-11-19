""" Create a five-element list containing 67, 12, 46, 43 and 13, then use list method index to search for a 43 and 44.
    Ensure that no ValueError occurs when searching for 44. """

five_element = [67, 12, 46, 43]

key = float(input('Please enter a number to search for:'))

if key in five_element:
    print(f'Found {key} at index {five_element.index(key)}')
else:
    print(f'Number {key} not found')

