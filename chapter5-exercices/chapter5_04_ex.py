""" Create a tuple high_low representing a day of the week (a string) and its high and low temperatures (integers),
    display its string representation, then perform the following tasks in an interactive IPython session:

    Use the [] operator to access and display the high_low tuple’s elements.

    Unpack the high_low tuple into the variables day and high.
    What happens and why? """

high_low = ('Monday', (21, 30))
day, high = high_low
print(f"It's {day} and the temperatures are between the followings:  High: {high[0]} - Low: {high[1]}")
