""" 3.16 (Nested Control Statements)
    Use a loop to find the two largest values of 10 numbers entered. """
from readline import clear_history

#initialization phase:

number = int(input('Enter how many numbers do you want so we can find the first two largest numbers: '))
largest_st = 0
largest_nd = 0
a = []

for i in range(1, number + 1):
    number = float(input(f'Enter number {i}: '))
    a += [number]

a = list(reversed(sorted(a)))
print(f'First largest number: {a[0]} and second largest number: {a[1]}')






