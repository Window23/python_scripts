""" (Is a Sequence Sorted?) Create a function is_ordered that receives a sequence and returns True if the elements are in sorted order.
    Test your function with sorted and unsorted lists, tuples and strings. """

def is_ordered(sequence):
    """Return True if the elements of the sequence are sorted in ascending order."""
    seq_list = list(sequence)
    return seq_list == sorted(seq_list)


# --- Testing with lists, tuples, and strings ---
print(is_ordered([1, 2, 3, 4]))     # True
print(is_ordered([3, 2, 1]))        # False

print(is_ordered((1, 2, 3)))        # True
print(is_ordered((3, 1, 2)))        # False

print(is_ordered("abc"))            # True
print(is_ordered("cba"))            # False
