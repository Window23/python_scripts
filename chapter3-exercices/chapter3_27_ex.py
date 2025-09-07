""" 3.27 (World Population Growth)
    World population has grown considerably over the centuries.
    Continued growth could eventually challenge the limits of breathable air, drinkable water, arable land and other limited resources.
    There’s evidence that growth has been slowing in recent years and that world population could peak some time this century, then start to decline.

    For this exercise, research world population growth issues. T
    his is a controversial topic, so be sure to investigate various viewpoints.
    Get estimates for the current world population and its growth rate.
    Write a script that calculates world population growth each year for the next 100 years, using the simplifying assumption that the current growth rate will stay constant .
    Print the results in a table.
    The first column should display the year from 1 to 100.
    The second column should display the anticipated world population at the end of that year.
    The third column should display the numerical increase in the world population that would occur that year.
    Using your results, determine the years in which the population would be double and eventually quadruple what it is today. """

previous_population_number = float(input("Enter the previous population number: "))
current_population_number = float(input("Enter the current population number: "))
growth_rate = (current_population_number - previous_population_number) / previous_population_number * 100

print(f'year     anticipated population      increased population')
for i in range(1, 101):
    current_population_number += growth_rate
    difference = current_population_number - previous_population_number
    previous_population_number = current_population_number
    print(f"{i:>4} {growth_rate + current_population_number:>26.2f} {difference:>25.2f}")











