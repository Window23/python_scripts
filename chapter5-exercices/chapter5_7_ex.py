""" (Palindrome Tester)
    A string that’s spelled identically backward and forward, like 'radar', is a palindrome.
    Write a function is_palindrome that takes a string and returns True if it’s a palindrome and False otherwise.
    Use a stack (simulated with a list as we did in Section 5.11) to help determine whether a string is a palindrome.
    Your function should ignore case sensitivity (that is, 'a' and 'A' are the same), spaces and punctuation. """

stringup = str(input("Enter a string to verify if it'a palindrome or not:"))

length_string = len(stringup)

def is_palindrome(arg):
    if length_string % 2 == 0:
        length_string_mid = length_string // 2
    else:
        length_string_mid = length_string // 2 + 1
    string_final = list(arg)
    first_part_string = []
    second_part_string = []
    for x in range(length_string_mid):
        first_part_string.append(stringup[x])
        second_part_string.append(string_final.pop())
    return first_part_string, second_part_string

a, b = is_palindrome(stringup)
first_check = a
second_check = b

if first_check == second_check:
    print("Palindrome")
else:
    print("Not Palindrome")

