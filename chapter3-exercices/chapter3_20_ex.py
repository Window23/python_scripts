""" 3.20 (Binary-to-Decimal Conversion)
    Input an integer containing 0s and 1s (i.e., a “binary” integer) and display its decimal equivalent.
    The online appendix, “Number Systems,” discusses the binary number system.
    [Hint: Use the modulus and division operators to pick off the “binary” number’s digits one at a time from right to left.
    Just as in the decimal number system, where the rightmost digit has the positional value 1 and
    the next digit to the left has the positional value 10, then 100, then 1000, etc., in the binary number system,
    the rightmost digit has the positional value 1, the next digit to the left has the positional value 2, then 4, then 8, etc.
    Thus, the decimal number 234 can be interpreted as 2 * 100 + 3 * 10 + 4 * 1.
    The decimal equivalent of binary 1101 is 1 * 8 + 1 * 4 + 0 * 2 + 1 * 1.] """

#initialization phase:
length_number  = int(input('Enter the length of the number system: '))
total = 0
total_list = []

for n in range(0, length_number):
    digit = int(input(f'Enter the {n + 1} digit(from right to left): '))
    if digit != 0 and digit != 1:
        digit = int(input(f'Enter the {n + 1} digit again(0 or 1, only): '))
    elif digit == 1:
       total += 2 ** n
       total_list += [digit]
    else:
        total += 0
        total_list += [digit]

print(f'The decimal equivalent of binary {list(reversed(total_list))}  is {total}')





