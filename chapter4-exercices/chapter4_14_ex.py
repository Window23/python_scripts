""" (Computer-Assisted Instruction)
    Computer-assisted instruction (CAI) refers to the use of computers in education.
    Write a script to help an elementary school student learn multiplication.
    Create a function that randomly generates and returns a tuple of two positive one-digit integers.
    Use that function’s result in your script to prompt the user with a question, such as

    How much is 6 times 7?

    For a correct answer, display the message "Very good!" and ask another multiplication question.
    For an incorrect answer, display the message "No.
    Please try again." and let the student try the same question repeatedly until the student finally gets it right. """

import random as rnd

variables = (rnd.randrange(10), rnd.randrange(10))
choice = int(input('Which type of calculations do you need/want to perform with a single digit?\nFor addition press 1\nFor subtraction press 2\nFor multiplication press 3\nFor division press 4\n'))

#initialization phase for multiplication
def elementary_multiplication(args):
    var1, var2 = args
    print(var1, var2)
    product = var1 * var2
    result = float(input(f'How much is {var1} times {var2}?'))

    if result == product:
        print('Verry good!')
    else:
        print('No. Please try again.')

    while result != product:
        result = float(input(f'How much is {var1} times {var2}?'))
        if result == product:
            print('Verry good!')
            break
    want_continuation = str(input('Would you like to continue with more examples (yes/no)?'))
    choice = int(input('Which type of calculations do you need/want to perform with a single digit?\nFor addition press 1\nFor subtraction press 2\nFor multiplication press 3\nFor division press 4\n'))

    return choice, want_continuation

#initialization phase for addition
def elementary_addition(args):
    var1, var2 = args
    print(var1, var2)
    addition = var1 + var2
    result = float(input(f'How much is {var1} added with {var2}?'))

    if result == addition:
        print('Verry good!')
    else:
        print('No. Please try again.')

    while result != addition:
        result = float(input(f'How much is {var1} added with  {var2}?'))
        if result == addition:
            print('Verry good!')
            break
    want_continuation = str(input('Would you like to continue with more examples (yes/no)?'))
    choice = int(input('Which type of calculations do you need/want to perform with a single digit?\nFor addition press 1\nFor subtraction press 2\nFor multiplication press 3\nFor division press 4\n'))
    return choice, want_continuation

#initialization phase for subtraction
def elementary_subtraction(args):
    var1, var2 = args
    print(var1, var2)
    if var1 > var2:
        subtraction = var1 - var2
        result = float(input(f'How much is {var1} minus {var2}?'))
    else:
        subtraction = var2 - var1
        result = float(input(f'How much is {var2} minus {var1}?'))


    if result == subtraction:
        print('Verry good!')
    else:
        print('No. Please try again.')

    while result != subtraction:
        if var1 > var2:
            subtraction = var1 - var2
            result = float(input(f'How much is {var1} minus {var2}?'))
        else:
            subtraction = var2 - var1
            result = float(input(f'How much is {var2} minus {var1}?'))

        if result == subtraction:
            print('Verry good!')
            break
    want_continuation = str(input('Would you like to continue with more examples (yes/no)?'))
    choice = int(input('Which type of calculations do you need/want to perform with a single digit?\nFor addition press 1\nFor subtraction press 2\nFor multiplication press 3\nFor division press 4\n'))
    return choice, want_continuation

#initialization phase for division
def elementary_division(args):
    var1, var2 = args
    print(var1, var2)
    if var1 > var2:
        division = var1 / var2
        result = float(input(f'How much is {var1} divided by {var2}?'))
    else:
        division = var2 / var1
        result = float(input(f'How much is {var2} divided by {var1}?'))

    if result == division:
        print('Verry good!')
    else:
        print('No. Please try again.')

    while result != division:
        if var1 > var2:
            division = var1 / var2
            result = float(input(f'How much is {var1} divided by {var2}?'))
        else:
            division = var2 / var1
            result = float(input(f'How much is {var2} divided by {var1}?'))

        if result == division:
            print('Verry good!')
            break
    want_continuation = str(input('Would you like to continue with more examples (yes/no)?'))
    choice = int(input('Which type of calculations do you need/want to perform with a single digit?\nFor addition press 1\nFor subtraction press 2\nFor multiplication press 3\nFor division press 4\n'))
    return choice, want_continuation


while choice in range(1,5):
    if choice == 1:
        choice_1 = elementary_addition(variables)
        variables = (rnd.randrange(10), rnd.randrange(10))
    if choice == 2:
        choice_2 = elementary_subtraction(variables)
        variables = (rnd.randrange(10), rnd.randrange(10))
    if choice == 3:
        choice_3 = elementary_multiplication(variables)
        variables = (rnd.randrange(10), rnd.randrange(10))
    if choice == 4:
        choice_4 = elementary_division(variables)
        variables = (rnd.randrange(10), rnd.randrange(10))
    if choice == 0:
        break
    else:
        print('Not a valid input. Please try again..\nBe aware that for ending type "0".')

