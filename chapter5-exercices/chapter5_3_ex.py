"""  Create a string called alphabet containing 'abcdefghijklmnopqrstuvwxyz', then perform the following separate slice operations to obtain:
    The first half of the string using starting and ending indices.
    The first half of the string using only the ending index.
    The second half of the string using starting and ending indices.
    The second half of the string using only the starting index.
    Every second letter in the string starting with 'a'.
    The entire string in reverse.
    Every third letter of the string in reverse starting with 'z'."""

#initial phase - Create a string called alphabet containing 'abcdefghijklmnopqrstuvwxyz', then perform the following separate slice operations to obtain
alphabet = ('abcdefghijklmnopqrstuvwxyz')

#processing phase1 - obtain The first half of the string using starting and ending indices.
print(alphabet[0:len(alphabet)//2])

#processing phase2 - obtain The first half of the string using only the ending index.
print(alphabet[:len(alphabet)//2])

#processing phase3 - obtain The second half of the string using starting and ending indices.
print(alphabet[len(alphabet)//2:len(alphabet)])

#processing phase4 - obtain The second half of the string using only the starting index.
print(alphabet[len(alphabet)//2:])

#processing phase5 - obtain Every second letter in the string starting with 'a'.
print(alphabet[::2])

#processing phase6 - obtain The entire string in reverse.
print(alphabet[::-1])

#processing phase7 - obtain Every third letter of the string in reverse starting with 'z'.
print(alphabet[::-3])