""" (Finding the People with a Specified Last Name)
    Create a list of tuples containing first and last names. Use filter to locate the tuples containing the last name Jones.
    Ensure that several tuples in your list have that last name. """

#initialization phase..

how_many_pople = int(input("How many people to find? "))

def create_list_of_tuple(arg):
    items = []
    for item in range(1, arg + 1):
        (first_name, last_name) = (str(input(f"Please enter first name for person number {item} ")).lower(),
                                   str(input(f"Please enter last name for person number {item} ")).lower())
        items.append((first_name, last_name))
    return items

filter_key = str(input("Please enter last name for person number to filter: ")).lower()
a = list(filter(lambda y: y[1] == filter_key, create_list_of_tuple(how_many_pople)))
print(a)