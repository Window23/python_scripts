""" 3.23 (Validating Indentation) The file validate_indents.py in this chapter’s ch03 examples folder contains the following code with incorrect indentation:
    grade = 93

    if grade >= 90:
        print('A')
     print('Great Job!')
       print('Take a break from studying')
    The Python Standard Library includes a code indentation validator module named tabnanny,
    which you can run as a script to check your code for proper indentation—this is one of many static code analysis tools.
    Execute the following command in the ch03 folder to see the results of analyzing validate_indents.py:

    ### python -m tabnanny validate_indents.py
    Suppose you accidentally aligned the second print statement under the i in the if keyword.
    What kind of error would that be? Would you expect tabnanny to flag that as an error? """