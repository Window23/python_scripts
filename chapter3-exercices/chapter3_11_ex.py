""" 3.11 (Miles Per Gallon)
    Drivers are concerned with the mileage obtained by their automobiles.
    One driver has kept track of several tankfuls of gasoline by recording miles driven and gallons used for each tankful.
    Develop a sentinel-controlled-repetition script that prompts the user to input the miles driven and gallons used for each tankful.
    The script should calculate and display the miles per gallon obtained for each tankful.
    After processing all input information, the script should calculate and display the combined miles per gallon obtained for all tankfuls
    (that is, total miles driven divided by total gallons used).

    Enter the gallons used (-1 to end): 12.8
    Enter the miles driven: 287
    The miles/gallon for this tank was 22.421875
    Enter the gallons used (-1 to end): 10.3
    Enter the miles driven: 200
    The miles/gallon for this tank was 19.417475
    Enter the gallons used (-1 to end): 5
    Enter the miles driven: 120
    The miles/gallon for this tank was 24.000000
    Enter the gallons used (-1 to end): -1
    The overall average miles/gallon was 21.601423 """

#initialization phase:

gallons_used = 0
gallons_used_total = 0
miles_driven_total = 0

while gallons_used >= 0:
    gallons_used = float(input("Enter the gallons used: "))
    miles_driven = float(input("Enter the miles driven: "))
    print(f'The miles/gallons for this tank was {miles_driven/gallons_used}.')
    miles_driven_total += miles_driven
    gallons_used_total += gallons_used

overall = miles_driven_total / gallons_used_total

print(f'The overall average miles/gallon was {overall}')
