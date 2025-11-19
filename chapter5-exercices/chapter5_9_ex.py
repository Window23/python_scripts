""" (Summarizing Letters in a String) Write a function summarize_letters that receives a string and returns a list of tuples
    containing the unique letters and their frequencies in the string. Test your function and display each letter with its frequency.
    Your function should ignore case sensitivity (that is, 'a' and 'A' are the same) and ignore spaces and punctuation.
    When done, write a statement that says whether the string has all the letters of the alphabet. """

string_ini = sorted(list(str(input("Enter a string: ")).lower().strip()))

def summarize_letters(arg):
    string_mid = []
    for letter in arg:
        a = letter, arg.count(letter)
        string_mid.append(a)
    string_final = sorted(set(string_mid))
    return string_final

print(summarize_letters(string_ini))


