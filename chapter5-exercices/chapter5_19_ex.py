""" (Display a Two-Dimensional List in Tabular Format)
    Define a function named display_table that receives a two-dimensional list and displays its contents in tabular format.
    List the column indices as headings across the top, and list the row indices at the left of each row. """

how_many_rows = int(input("How many rows would you like to display? "))
how_many_columns = int(input("How many columns would you like? "))



def generate_rows():
    two_dim_list = []
    for row in range(how_many_rows):
        a = []
        for column in range(how_many_columns):
            a.append(int(input(f'Please enter value: ')))
        two_dim_list.append(a)
    return two_dim_list

def display_table(arg):
    print("The contents of the table: ")
    for item in range(how_many_columns):
        print(f" {item:^1}", end=' ')
    print()
    for i, item in enumerate(arg):
        print(f'{i}', end= ' ')
        for value in item:
            print(f"{value:^2}", end=' ')
        print()
    return print(f'\n')

display_table(generate_rows())
