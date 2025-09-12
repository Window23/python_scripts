""" Let’s produce 6 mil random integers in the range 1–6 to simulate rolling a six-sided die: """

import random

def roll_normal_dice():
    roll_die_list = []
    frequency_1 = 0
    frequency_2 = 0
    frequency_3 = 0
    frequency_4 = 0
    frequency_5 = 0
    frequency_6 = 0
    for roll in range(60_000_000):
        n = random.randrange(1, 7)
        roll_die_list.append(n)
        if n == 1:
            frequency_1 += 1
        elif n == 2:
            frequency_2 += 1
        elif n == 3:
            frequency_3 += 1
        elif n == 4:
            frequency_4 += 1
        elif n == 5:
            frequency_5 += 1
        elif n == 6:
            frequency_6 += 1
    print(f'Face{"Frequency":>13}')
    print(f'{1:>4}{frequency_1:>13}')
    print(f'{2:>4}{frequency_2:>13}')
    print(f'{3:>4}{frequency_3:>13}')
    print(f'{4:>4}{frequency_4:>13}')
    print(f'{5:>4}{frequency_5:>13}')
    print(f'{6:>4}{frequency_6:>13}')

    return

roll_normal_dice()