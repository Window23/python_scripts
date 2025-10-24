""" (Modified average Function)
    The average function we defined in Section 4.11 can receive any number of arguments.
    If you call it with no arguments, however, the function causes a ZeroDivisionError.
    Reimplement average to receive one required argument and the arbitrary argument list argument *args, and update its calculation accordingly.
    Test your function.
    The function will always require at least one argument, so you’ll no longer be able to get a ZeroDivisionError.
    When you call average with no arguments, Python should issue a TypeError indicating "average() missing 1 required positional argument. """

def average(*args):
    if len(args) == None:
        args = []
        number_of_args = int(input("How many arguments would you like to average? "))
        for value in range(number_of_args):
            value = float(input(f"Enter the {value + 1} number for adding to the list of arguments so we can calculate the average value of that list: "))
            args.append(value)
    else:
        args = []
        number_of_args = int(input("How many arguments would you like to average? "))
        for value in range(number_of_args):
            value = float(input(f"Enter the {value + 1} number for adding to the list of arguments so we can calculate the average value of that list: "))
            args.append(value)
    return print(f'The average of the following numbers {args} is {sum(args) / len(args)}')

average()

