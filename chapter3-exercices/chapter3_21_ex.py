""" 3.21 (Calculate Change Using Fewest Number of Coins)
    Write a script that inputs a purchase price of a dollar or less for an item.
    Assume the purchaser pays with a dollar bill.
    Determine the amount of change the cashier should give back to the purchaser.
    Display the change using the fewest number of pennies, nickels, dimes and quarters.
    For example, if the purchaser is due 73 cents in change, the script would output: """
from os import WCONTINUED

from readline import clear_history

#initialization phase:
quarters = 25
dimes = 10
nickels = 5
pennies = 1

total_quarters = 0
total_dimes = 0
total_nickels = 0
total_pennies = 0

number  = int(input("Enter purchase price: "))

while number > 0:
    total_quarters = number // quarters
    number = number % quarters
    total_dimes = number // dimes
    number = number % dimes
    total_nickels = number // nickels
    number = number % nickels
    total_pennies = number // pennies
    number = number % pennies




if total_quarters > 0:
    print("Total quarters: ", total_quarters)
if total_dimes > 0:
    print("Total dimes: ", total_dimes)
if total_nickels > 0:
    print("Total nickels: ", total_nickels)
if total_pennies > 0:
    print("Total pennies: ", total_pennies)
else:
    None






