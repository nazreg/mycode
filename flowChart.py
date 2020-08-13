#!/usr/bin/env python3
import sys

"""Does it move? Engineering FlowChart || Author: Marcelo Nazario"""

# Declare variables with questions
question1 = "Does it move? \ntype yes or no here >>> "
question2 = "Should it? "


# While loop to assign user answers from prompt
def asker():
    while True:
        answer1 = input(question1).lower().strip()
        if answer1 == "q":
            sys.exit()
        elif answer1 == "yes" or answer1 == "no":
            break
        else:
            print("Invalid input. Try again.")
    while True:
        answer2 = input(question2).lower().strip()
        if answer1 == "q":
            sys.exit()
        elif answer2 == "yes" or answer2 == "no":
            break
        else:
            print("Invalid input. Try again.")
    return [answer1, answer2]


# Define function to print something base on user input
def response(answers):
    if answers[0] == "yes" and answers[1] == "yes":
        print("No problem here.")
    elif answers[0] == "yes" and answers[1] == "no":
        print("Use duct tape!")
    elif answers[0] == "no" and answers[1] == "no":
        print("No problem here.")
    elif answers[0] == "no" and answers[1] == "yes":
        print("Use WD40")


# Define a main function
def main():
    response(asker())

# Run main function
main()
