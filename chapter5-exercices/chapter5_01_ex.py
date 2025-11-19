""" Create a function cube_list that cubes each element of a list.
    Call the function with the list numbers containing 1 through 10.
    Show numbers after the call. """


def cube_list(args):
    a = []
    for num in range(len(args)):
        a.append(args[num] ** 3)
    return print(a)

numbers = [x for x in range(1, 11)]

cube_list(numbers)