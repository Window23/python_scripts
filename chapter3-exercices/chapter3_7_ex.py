""" 3.7 (Table of Squares and Cubes)
    In Exercise 2.8, you wrote a script to calculate the squares and cubes of the numbers from 0 through 5,
    then printed the resulting values in table format. Reimplement your script using a for loop and
    the f-string capabilities you learned in this chapter to produce the following table with the numbers right aligned in each column. """

#initialization phase:
print('number  square  cube')

#processing phase:
for x in range(6):
    print(f'{x:>6}{x ** 2:>8}{x ** 3:>6}')
