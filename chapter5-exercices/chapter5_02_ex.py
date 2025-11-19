""" Use an empty list named characters and a += augmented assignment statement to convert the string 'Birthday' into a list of its characters. """





def convert_string_in_list(*args):
    """ converting a string into a list of its characters. """
    characters = []
    for character in range(len(args)):
        characters.append(args[character].lower())
    return characters

strings = 'Birthday'

print(convert_string_in_list(*strings))
