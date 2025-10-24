""" Replace the ***s in the seconds_since_midnight function so that it returns the number of seconds since midnight.
    The function should receive three integers representing the current time of day.
    Assume that the hour is a value from 0 (midnight) through 23 (11 PM) and that the minute and second are values from 0 to 59.
    Test your function with actual times.
    For example, if you call the function for 1:30:45 PM by passing 13, 30 and 45, the function should return 48645. """

def seconds_since_midnight(*args):
    hour_in_seconds = args[0] * 3600
    minute_in_seconds = args[1] * 60
    if args[3] == 'PM':
        hour_in_seconds = 12 * 3600 + (args[0] * 3600)
    else:
        hour_in_seconds = args[0] * 3600
    return print(hour_in_seconds + minute_in_seconds + args[2])

seconds_since_midnight(1, 30, 45, 'PM')
