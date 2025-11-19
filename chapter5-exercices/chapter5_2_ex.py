""" (Iteration Order) Create a 2-by-3 list, then use a nested loop to:
    Set each element’s value to an integer indicating the order in which it was processed by the nested loop.
    Display the elements in tabular format.
    Use the column indices as headings across the top, and the row indices to the left of each row. """

#initialization phase - defining the rows and columns.
(row, col) = (2, 3)

#initialization phase - defining the table with zeroes.
table = [[0 for c in range(col)] for r in range(row)]

#number1 -    Set each element’s value to an integer indicating the order in which it was processed by the nested loop.
total = 1
for r in range(row):
    for c in range(col):
        table[r][c] = total
        total += 1

#number2 - Display the elements in tabular format - print column headings.
print("    ", end="")
for c in range(col):
    print(f'{c:4}', end='')
print()

#number2 - Display the elements in tabular format - print rows in the left.
for r in range(row):
    print(f'{r:2} |', end='')
    for c in range(col):
        print(f'{table[r][c]:4}', end='')
    print()






