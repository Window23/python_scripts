""" Create a list called numbers containing the values from 1 through 15, then use slices to perform the following operations consecutively:
    Select number’s even integers.
    Replace the elements at indices 5 through 9 with 0s, then show the resulting list.
    Keep only the first five elements, then show the resulting list.
    Delete all the remaining elements by assigning to a slice. Show the resulting list. """

#Create a list called numbers containing the values from 1 through 15
numbers = list(range(1,16))
print(f'Create a list called numbers containing the values from 1 through 15: {numbers}')

#Select number’s even integers.
print(f'Select number’s even integers. {numbers[1:len(numbers):2]}')

#Replace the elements at indices 5 through 9 with 0s, then show the resulting list.
numbers[5:10] = [0] * len(numbers[5:10])
print(f'Replace the elements at indices 5 through 9 with 0s, then show the resulting list. {numbers[5:10]}')

#Keep only the first five elements, then show the resulting list.
numbers[5:] = []
print(f'Keep only the first five elements, then show the resulting list. {numbers}')

numbers[:] = []
print(f'Delete all the remaining elements by assigning to a slice. Show the resulting list. {numbers}')
