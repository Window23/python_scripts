""" 3.14 (Challenge: Approximating the Mathematical Constant π)
    Write a script that computes the value of π from the following infinite series.
    Print a table that shows the value of π approximated by one term of this series, by two terms, by three terms, and so on.
    How many terms of this series do you have to use before you first get 3.14? 3.141? 3.1415? 3.14159? """

#initialization phase:
number = int(input('Enter how many digits you need/want to check for the pi number: '))
pi_init = 4
pi_st = 0
pi_nd = 0
number_st = 3 + number
number_nd = 5 + number

#conculation phase:
for n in range(3, number_st + 1, 4):
    term_neg = -(4 / n)
    pi_st += term_neg
    print(f'{pi_st:.{number + 1}}')
    for n in range(5, number_nd + 1, 4):
        term_poz = 4 / n
        pi_nd +=  term_poz
        print(f'{pi_nd:.{number + 1}}')
    pi = pi_init + pi_st + pi_nd
    print('pi =', pi)
