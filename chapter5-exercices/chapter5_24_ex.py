""" 5.25 (Card Playing: Evaluating Poker Hands)
    Modify Exercise 5.24 to deal a five-card poker hand as a list of five card tuples.
    Then create functions (i.e., is_pair, is_two_pair, is_three_of_a_kind, …) that determine whether the hand they receive as an argument contains groups of cards, such as:

    one pair
    two pairs
    three of a kind (e.g., three jacks)
    a straight (i.e., five cards of consecutive face values)
    a flush (i.e., all five cards of the same suit)
    a full house (i.e., two cards of one face value and three cards of another)
    four of a kind (e.g., four aces)
    straight flush (i.e., a straight with all five cards of the same suit)
    … and others.

    See https://en.wikipedia.org/wiki/List_of_poker_hands for poker-hand types and how they rank with respect to one another. For example, three of a kind beats two pairs. """

import random

ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14)

def deck_initialization():
    faces = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']

    deck = [(x, y) for x in faces for y in suits]
    random.shuffle(deck)
    return deck

def display_five_cards(arg):
    cards = []

    for i in range(5):
        cards.append(arg[i])
    for i, card in enumerate(cards):
        if i + 1 == 1:
            print(f"{i + 1}st card is {card[0]} of {card[1]}")
        elif i + 1 == 2:
            print(f"{i + 1}nd card is {card[0]} of {card[1]}")
        elif i + 1 == 3:
            print(f"{i + 1}rd card is {card[0]} of {card[1]}")
        elif i + 1 == 4:
            print(f"{i + 1}th card is {card[0]} of {card[1]}")
        elif i + 1 == 5:
            print(f"{i + 1}th card is {card[0]} of {card[1]}")
    return cards


def is_pair(arg):
    face = []
    for faces, suit in arg:
        face.append(faces)
    cards = list(set(i for i in face if face.count(i) == 2))
    print(cards)
    if len(cards) > 0:
        printing = [x for x in arg if x[0] == cards[0]]
        print(f"We've got a pair of the following cards: {printing}")
    else:
        return print(f"Could not find a pair in {arg}.")


def two_pairs(arg):
    faces = []
    for face, suit in arg:
        faces.append(face)
    cards = list(set(i for i in faces if faces.count(i) == 2))
    print(cards if len(cards) > 1 else f"Could not find a pair in {arg}.")
    if len(cards) > 1:
        printing_two_pairs = []
        for item in cards:
            for face, suit in enumerate(arg):
                if item in suit:
                    printing_two_pairs.append(suit)
        print(f"Found the following pairs: {printing_two_pairs}.")
    return


def three_of_a_kind(arg):
    faces = []
    for face, suit in arg:
        faces.append(face)
    cards = list(set(x for x in faces if faces.count(x) == 3))
    print(cards if len(cards) > 0 else f"Could not find a three of a kind pair in {arg}.")
    if len(cards) > 0:
        printing_three_of_a_kind = []
        for item in cards:
            for face, suit in enumerate(arg):
                if item in suit:
                    printing_three_of_a_kind.append(suit)
        print(f"Found the following three of a kind: {printing_three_of_a_kind}")
    return

def four_of_a_kind(arg):
    faces = []
    for face, suit in arg:
        faces.append(face)
    cards = list(set(i for i in faces if faces.count(i) == 4))
    print(cards if len(cards) > 0 else f"Could not find a four of a kind pair in {arg}.")
    if len(cards) > 0:
        printing_four_of_a_kind = []
        for item in cards:
            for face, suit in enumerate(arg):
                if item in suit:
                    printing_four_of_a_kind.append(suit)
        print(f"Found the following four of a kind: {printing_four_of_a_kind}")
    return



if __name__ == '__main__':
    desk = deck_initialization()
    print("displayed 5 shuffled cards: ")
#    print(display_five_cards(deck_initialization()))
#    print(is_pair(display_five_cards(deck_initialization())))
#    print(two_pairs(display_five_cards(deck_initialization())))
#    print(three_of_a_kind(display_five_cards(deck_initialization())))
    print(four_of_a_kind(display_five_cards(deck_initialization())))

