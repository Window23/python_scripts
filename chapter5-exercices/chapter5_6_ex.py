""" (Sieve of Eratosthenes) A prime number is an integer greater than 1 that’s evenly divisible only by itself and 1.
    The Sieve of Eratosthenes is an elegant, straightforward method of finding prime numbers.
    The process for finding all primes less than 1000 is:

    1.Create a 1000-element list primes with all elements initialized to True.
    List elements with prime indices (like 2, 3, 5, 7, 11, …) will remain True.
    All other list elements will eventually be set to False.

    2.Starting with index 2, if a given element is True iterate through the rest of the list
    and set to False every element in primes whose index is a multiple of the index for the element we’re currently processing.
    For list index 2, all elements beyond element 2 in the list that have indices which are multiples of 2 (i.e., 4, 6, 8, 10, …, 998) will be set to False.

    3.Repeat Step (b) for the next True element.
    For list index 3 (which was initialized to True), all elements beyond element 3 in the list
    that have indices which are multiples of 3 (i.e., 6, 9, 12, 15, …, 999) will be set to False; and so on.
    A subtle observation (think about why this is true): The square root of 999 is 31.6,
    you’ll need to test and set to False only all multiples of 2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29 and 31.
    This will significantly improve the performance of your algorithm, especially if you decide to look for large prime numbers.

    When this process completes, the list elements that are still True indicate that the index is a prime number.
    These indices can be displayed. Use a list of 1000 elements to determine and display the prime numbers less than 1000.
    Ignore list elements 0 and 1. [As you work through the book, you’ll discover other Python capabilities that will enable you to cleverly reimplement this exercise.] """

import math

#initialization phase: Declaring the list of the first n numbers..

n_numbers = int(input("Please enter a number for guessing all the primes numbers: "))
list_numbers = [x for x in range(n_numbers + 1)]

#processing phase:
def list_d(arg):
    c = []
    for index, value in enumerate(arg):
        d = [x for x in range(2, int(math.sqrt(value)) + 1)]
        if len(d) == 0:
            response = 'true'
        else:
            response_d = []
            for item in d:
                z = value % item
                response_d.append(z)
                if 0 in response_d:
                    response = 'false'
                else:
                    response = 'true'
        b = (index, response)
        c.append(b)
    return c

print(list_d(list_numbers))






