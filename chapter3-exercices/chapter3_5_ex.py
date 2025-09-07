""" 3.5 (if…else Statements) Reimplement the script of Fig2.1.
    using three if…else statements rather than six if statements.
    [Hint: For example, think of == and != as “opposite” tests.] ."""

number1 = float(input("Enter the first number to be compared: "))
number2 = float(input("Enter the second number to be compared: "))

if number1 > number2 and number1 != number2:
    print(f'The numbers are different and number {number1} > number {number2}.')
if number1 == number2:
    print(f'The numbers are equal and number {number2} = number {number1}.')
else:
    print(f'The numbers are different and number {number2} > number {number1}.')