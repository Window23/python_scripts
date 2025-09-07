""" 3.8 (Arithmetic, Smallest and Largest)
    In Exercise 2.10, you wrote a script that input three integers, then displayed the sum, average, product, smallest and largest of those values.
    Reimplement your script with a loop that inputs four integers. """

#initialization phase:
numbers = int(input('Enter how many numbers you need for calculating the sum, average, product, smallest and largest: '))
total = 0
product = 1
largest = None
smallest = None

#processing phase:
for n in range(1, numbers + 1):
    number = float(input(f'Enter number {n}: '))
    total += number
    product *= number
    if largest is None or number >= largest:
        largest = number
    if smallest is None or number <= smallest:
        smallest = number


average = total / numbers

#termination phase:
print(f'The sum of the numbers entered is {total}.')
print(f'The product of the numbers entered is {product}.')
print(f'The largest of the numbers entered is {largest}.')
print(f'The smallest of the numbers entered is {smallest}.')
print(f'The average of the numbers entered is {average}.')



