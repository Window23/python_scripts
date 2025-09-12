""" Calculate the square of number. """

number = float(input("Enter a number: "))
number_expo = float(input("Enter a number as exponent: "))

def raising(x, y):
    return x ** y

print(f'{raising(number, number_expo)} is the result from {number} raised by {number_expo}.')