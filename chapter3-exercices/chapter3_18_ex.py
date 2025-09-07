""" 3.18 (Challenge: Nested Looping)
    Modify your script from Exercise 3.17 to display all four patterns side-by-side
    (as shown above) by making clever use of nested for loops. Separate each triangle from the next by three horizontal spaces.
    [Hint: One for loop should control the row number.
    Its nested for loops should calculate from the row number the appropriate number of asterisks and spaces for each of the four patterns.] """

#initialization phase:

#initialization phase:
stars = int(input('Please enter the number of stars: '))

for a in range(1, stars + 1):
    for b in range(a):
        print('*', end=' ')
    for c in range(stars - a + 1):
        print(' ', end=' ')
    for d in range(stars - a + 1):
        print('*', end=' ')
    for e in range(a):
        print(' ', end=' ')
    for g in range(a):
        print(' ', end=' ')
    for h in range(stars - a + 1):
        print('*', end=' ')
    for j in range(stars - a):
        print(' ', end=' ')
    for k in range(a):
        print('*', end=' ')
    print()