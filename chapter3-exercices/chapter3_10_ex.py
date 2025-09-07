""" 3.10 (7% Investment Return)
    Reimplement Exercise 2.12 to use a loop that calculates and displays the amount of money you’ll have each year at the ends of years 1 through 30. """

p = 1000
r = 7 / 100


for n in range(1, 31, 1):
    a = (p *(1 + r) * n)
    print(f'Amount accumulated after {n} years:', a)