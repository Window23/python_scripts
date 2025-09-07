""" 3.29 (Intro to Data Science: Problem with the Median)
    For an odd number of values, to get the median you simply arrange them in order and take the middle value.
    For an even number, you average the two middle values.
    What problem occurs if those two values are different?
    answer.. it calculates the average between them"""
import statistics

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(statistics.median(a))
