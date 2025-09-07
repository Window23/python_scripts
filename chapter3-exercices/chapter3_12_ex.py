""" 3.12 (Palindromes)
    A palindrome is a number, word or text phrase that reads the same backwards or forwards.
    For example, each of the following five-digit integers is a palindrome:
    12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer
    and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate the number into its digits.] """

#initializatoin phase:

number = int(input('Enter a number to check if it is a palindrome or not: '))
length_number = len(str(number))
length_number_last = len(str(number))
number_init = number
number_last = number
checks = 1

print(f'The number of {number} have the length of {length_number} digits.')


while number > 0:
    number_ascend = number // (10 ** (length_number -1))
    number_descend = number_init  % (10 ** (length_number - (length_number - 1)))
    print(f'{number_ascend} - {number_descend} {checks:>4} check')
    if number_ascend == number_descend:
        checks += 1
    else:
        break
    number_init = number_init // (10 ** (length_number - (length_number - 1)))
    number = number % (10 ** (length_number - 1))
    length_number -= 1

if checks -1  == length_number_last:
    print(f'The number {number_last} is a palindrome.')
else:
    print(f'The number {number_last} is not a palindrome.')















