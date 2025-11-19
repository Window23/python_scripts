""" (Temperature Conversion) Implement a Fahrenheit function that returns the Fahrenheit equivalent of a Celsius temperature.
    Use the following formula:

    F = (9 / 5) * C + 32

    Use this function to print a chart showing the Fahrenheit equivalents of all Celsius temperatures in the range 0–100 degrees.
    Use one digit of precision for the results. Print the outputs in a neat tabular format. """

celsius_list = list(range(0, 101))
Fahrenheit_list = []

def fahrenheit(*args):
    for value in args:
        F = (9 / 5) * value + 32
        cel_to_fa = round(F, 1)
        Fahrenheit_list.append(cel_to_fa)
    return print(f'Fahrenheit list of all the first 100 degrees is {Fahrenheit_list}')

fahrenheit(*celsius_list)

