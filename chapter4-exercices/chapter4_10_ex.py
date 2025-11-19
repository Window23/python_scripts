""" (Guess the Number)
    Write a script that plays “guess the number.” Choose the number to be guessed by selecting a random integer in the range 1 to 1000.
    Do not reveal this number to the user.
    Display the prompt "Guess my number between 1 and 1000 with the fewest guesses:".
    The player inputs a first guess. If the guess is incorrect, display "Too high. Try again." or "Too low. Try again."
    as appropriate to help the player “zero in” on the correct answer, then prompt the user for the next guess.
    When the user enters the correct answer, display "Congratulations.
    You guessed the number!", and allow the user to choose whether to play again. """

import random as rnd

def random_number():
    """ method to generate a random number between 1 and 1000 """
    return rnd.randrange(1, 1000)

number  = (random_number())

def guess_gen_number():
    """ method to ask the user to guess the randomly generated number between 1 and 1000 """
    guess_number = float(input("Guess my number between 1 and 1000: "))
    while guess_number > 0:
        tries_left = 0
        tries_right = 0
        left_end = 1
        right_end = 1000
        if guess_number > number:
            print(f"Too high. Please try again. Be aware that the interval changed between {left_end} and {right_end}.")
            tries_right += 1
            right_end = guess_number
            guess_number = float(input(f"Guess my number between {left_end} and {right_end}: "))
        elif guess_number < number:
            print(f"Too low. Please try again. Be aware that the interval changed between {left_end} and {right_end}.")
            tries_left += 1
            left_end = guess_number
            guess_number = float(input(f"Guess my number between {left_end} and {right_end}: "))
        elif guess_number == number:
            tries = 1 + tries_right + tries_left
            print(f"Congratulations!!  You guessed the number in about {tries} tries.")
            break
    return tries

tries_number = guess_number = guess_gen_number()

if tries_number < 10:
    print("Either you know the secret or you got lucky!")
else:
    print("You should be able to do better!")
