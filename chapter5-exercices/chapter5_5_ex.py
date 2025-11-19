""" (Duplicate Elimination)
    Create a function that receives a list and returns a (possibly shorter) list containing only the unique values in sorted order.
    Test your function with a list of numbers and a list of strings. """

def unique_values(list1):
    return sorted(set(list1))

a = int(input("Please enter the list size: "))

c = []

for i in range(a):
    b = float(input("please enter a value to add to the list: "))
    c.append(b)

print(unique_values(c))


