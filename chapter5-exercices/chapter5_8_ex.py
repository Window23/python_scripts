""" (Anagrams) An anagram of a string is another string formed by rearranging the letters in the first.
    Write a script that produces all possible anagrams of a given string using only techniques that you’ve seen to this point in the book.
    [The itertools module provides many functions, including one that produces permutations.] """

import itertools

string_ini = str(input("Enter a string: "))

def anagrams(arg):
    anagrams = itertools.permutations(arg)
    return list(anagrams)

print(anagrams(string_ini))

