""" Let’s define a maximum function that determines and returns the
    largest of three values—the following session calls the function three times with integers,
    floating-point numbers and strings, respectively. """

value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))
value3 = float(input("Enter the third value: "))


def largest_three(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print(f'largest value of {value1}, {value2}, and {value3} is {largest_three(value1, value2, value3)}')
