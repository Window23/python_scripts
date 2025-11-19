""" (Summing the Triples of the Even Integers from 2 through 10)
    Starting with a list containing 1 through 10, use filter, map and sum to calculate the total of the triples of
    the even integers from 2 through 10. Reimplement your code with list comprehensions rather than filter and map. """

a = sum(list(map(lambda x: x * 3,list(filter(lambda x: x % 2 == 0, range(1, 10))))))
print(a)

b = sum(x * 3 for x in range(1, 10) if x % 2 == 0)
print(b)