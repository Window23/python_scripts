""" 5.24 (Card Shuffling and Dealing)
    In Exercises 5.24 through 5.26, you’ll use lists of tuples in scripts that simulate card shuffling and dealing.
    Each tuple represents one card in the deck and contains a face
    (e.g., 'Ace', 'Deuce', 'Three', …, 'Jack', 'Queen', 'King') and a suit (e.g., 'Hearts', 'Diamonds', 'Clubs', 'Spades').
    Create an initialize_deck function to initialize the deck of card tuples with 'Ace' through 'King' of each suit, as in



    deck = [('Ace', 'Hearts'), …, ('King', 'Hearts'),

        ('Ace', 'Diamonds'), …, ('King', 'Diamonds'),

        ('Ace', 'Clubs'), …, ('King', 'Clubs'),

        ('Ace', 'Spades'), …, ('King', 'Spades')]

    Before returning the list, use the random module’s shuffle function to randomly order the list elements. Output the shuffled cards in the following four-column format:
    A screen shot of an image that shows the use of a random module’s shuffle function and the output of the shuffled cards in a 4 column format. """

import random

def create_deck():
    faces = ['ace', 'deuce', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']

    deck = [(x, y) for x in suits for y in faces]

    random.shuffle(deck)
    return deck

def displying_deck(arg):
    for i, item in enumerate(arg, start=1):
        print(f"{item[0]} of {item[1]:<9}", end="\t")
        if i % 5 == 0:
            print()
    return print()


if __name__ == '__main__':
    deck = create_deck()
    print("shuffled cards:")
    displying_deck(deck)



