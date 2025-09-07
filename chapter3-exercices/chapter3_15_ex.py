""" 3.15 (Challenge: Approximating the Mathematical Constant e)
    Write a script that estimates the value of the mathematical constant e by using the formula below.
    Your script can stop after summing 10 terms. """

#initialization phase:

terms_number = int(input("Please ester how many terms do you want in the Euler's formula? "))
x = 1
euler_st = 1
euler_nd = 0

#calculation phase:
for m in range(1, terms_number + 1):
    x *= m
    euler_nd  += (1 / x)
    euler_formula = euler_st + euler_nd
    print("Euler's formula is: ", euler_formula)


