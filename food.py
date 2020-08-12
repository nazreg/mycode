#!/usr/bin/env python3

# docstring with description
"""
Find out if you are a carnivore or vegetarian
author = Marcelo Nazario
"""


# Declare carnivore variable to track user choices
carnivore = 0
# Declare vegetarian variable to track user choices
vegetarian = 0


# Write function asking user for a choice
def asker(f1, f2):
    global carnivore
    global vegetarian
    # Declare counter variable to track user input
    counter = 0
    while counter == 0:
        print("__________________________________________")
        food = input(f"1.{f1} \n2.{f2} \nType Here >>> ")
        print("__________________________________________")
        if food == "1":
            carnivore += 1
            counter += 1
        elif food == "2":
            vegetarian += 1
            counter += 1
        else:
            print("Not a valid choice, try again")
            print("__________________________________________")


# Print statement to give user instructions
print("__________________________________________")
print("Please type your preference using the number of the item:")

# Run function with arguments
asker("Steak", "Vegetarian Pizza")
asker("Chicken Salad", "Vegetarian Salad")
asker("Chicken Wings", "Veggie Stuffed Shells")

# Add total of questions answer
total = carnivore + vegetarian
# Calculate percentage
cpercent = carnivore / total * 100
vpercent = vegetarian / total * 100

# Print results using f string format
print(f"You are approximately {int(cpercent)}% carnivore and {int(vpercent)}% vegetarian.")

