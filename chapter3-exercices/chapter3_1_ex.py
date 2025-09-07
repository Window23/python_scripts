""" 3.1 (Validating User Input)
    Modify the script of Fig3.3.  to validate its inputs. For any input, if the value entered is other than 1 or 2, keep looping until the user enters a correct value.
    Use one counter to keep track of the number of passes, then calculate the number of failures after all the user’s inputs have been received."""

""" The program must process 10 test results. 
    We’ll use a for statement and the range function to control repetition.
    Each test result is a number—either a 1 or a 2. Each time the program reads a test result, the program must determine if the number is a 1 or a 2. 
    We test for a 1 in our algorithm. If the number is not a 1, we assume that it’s a 2. (An exercise at the end of the chapter considers the consequences of this assumption.)
    We’ll use two counters—one to count the number of students who passed the exam and one to count the number of students who failed.
    After the script processes all the results, it must decide if more than eight students passed the exam so that it can bonus the instructor. """


#initialization phase:
num_passes = 0
num_failures = 0

students = int(input("Enter the number of students who took the exam: "))

for x in range(students):
    grade = float(input("Enter grade: "))
    if grade >= 70:
        num_passes += 1
    elif grade >=0 and grade < 70:
        num_failures += 1
    else:
        grade = int(input("Enter a proper grade: "))
        if grade >= 70:
            num_passes += 1
        else:
            num_failures += 1

if num_failures > students // 3:
    print(f'{num_failures} failed to pass the exam of a total of {students} students')
else:
    print(f'{num_passes} passes the exam of a total of {students} students. Bonus to the instructor')