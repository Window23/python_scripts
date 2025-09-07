""" 3.17 (Nested Loops)
    Write a script that displays the following triangle patterns separately, one below the other.
    Separate each pattern from the next by one blank line. Use for loops to generate the patterns.
    Display all asterisks ( *) with a single statement of the form
    which causes the asterisks to display side by side.
    [Hint: For the last two patterns, begin each line with zero or more space characters.] """

#initialization phase:
stars = int(input('Please enter the number of stars: '))


for a in range(stars):
    for b in range(stars - a):
        print(' ', end=' ')
    for c in range(a):
        print('*', end=' ')
    print()
