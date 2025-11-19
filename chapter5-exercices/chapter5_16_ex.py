""" (Filter/Map Performance) With regard to the following code:
    numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
    list(map(lambda x: x ** 2,
    filter(lambda x: x % 2 != 0, numbers)))

    1. How many times does the filter operation call its lambda argument?
    2. How many times does the map operation call its lambda argument?
    3. If you reverse the filter and map operations, how many times does the map operation call its lambda argument?

    To help you answer the preceding questions, define functions that perform the same tasks as the lambdas.
    In each function, include a print statement so you can see each time the function is called.
    Finally, replace the lambdas in the preceding code with the names of your functions. """

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def filter_function(arg):
    numbers_filtered = []
    for number in arg:
        if number % 2 != 0:
            numbers_filtered.append(number)

    return numbers_filtered

def map_function(arg):
    numbers_mapped = []
    for number in arg:
        numbers_mapped.append(number ** 2)
    return numbers_mapped

def filter_map(arg):
    numbers_mapped = []
    numbers_filtered = []
    for number in arg:
        numbers_mapped.append(number ** 2)
        print(number ** 2, end =' ')
    print()

    for number in numbers_mapped:
        if number % 2 != 0:
            numbers_filtered.append(number)
            print(number, end=' ')
    print()
    return numbers_filtered

print(filter_function(numbers))
print(map_function(filter_function(numbers)))
print(filter_map(numbers))






