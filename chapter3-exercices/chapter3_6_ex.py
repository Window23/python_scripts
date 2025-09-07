""" 3.6 (Turing Test)
    The great British mathematician Alan Turing proposed a simple test to determine whether machines could exhibit intelligent behavior.
    A user sits at a computer and does the same text chat with a human sitting at a computer and a computer operating by itself.
    The user doesn’t know if the responses are coming back from the human or the independent computer.
    If the user can’t distinguish which responses are coming from the human and which are coming from the computer,
    then it’s reasonable to say that the computer is exhibiting intelligence.

    Create a script that plays the part of the independent computer, giving its user a simple medical diagnosis.
    The script should prompt the user with 'What is your problem?'
    When the user answers and presses Enter, the script should simply ignore the user’s input,
    then prompt the user again with 'Have you had this problem before (yes or no)?' If the user enters 'yes',
    print 'Well, you have it again.' If the user answers 'no', print 'Well, you have it now.'

    Would this conversation convince the user that the entity at the other end exhibited intelligent behavior?
    Why or why not? """

#initialization phase:
ask_about_problem = str(input('What is your problem? '))
ask_about_ocurrence = str(input('Have you had this problem before? (yes or not, only) '))

#processing phase:
if ask_about_ocurrence.lower() == 'yes':
    print('Well, you have it again. ')
else:
    print('Well, you have it now. ')


while ask_about_ocurrence.lower() != 'yes' or ask_about_ocurrence.lower() != 'no':
    ask_about_ocurrence = str(input('Please enter an yes or not response'))
    if ask_about_ocurrence.lower() == 'yes':
        print('Well, you have it again. ')
    else:
        print('Well, you have it now. ')
        break

