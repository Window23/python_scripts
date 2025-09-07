""" 3.9 (Separating the Digits in an Integer)
    In Exercise 2.11, you wrote a script that separated a five-digit integer into its individual digits and displayed them.
    Reimplement your script to use a loop that in each iteration “picks off” one digit (left to right) using the // and % operators, then displays that digit. """
from sys import unraisablehook

#initialization phase:
number_digits = int(input("Please enter how many digits you would like to have your number: "))
number = int(input('Enter a five-digit number: '))


#calculation phase:
while number > 0:
    number_init = number // (10 ** (number_digits - 1))
    print(number_init, end=' ')
    number_digits = number_digits - 1
    number = number % (10 ** (number_digits))

print()
