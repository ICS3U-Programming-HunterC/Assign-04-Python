#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 20, 2022
# This program asks the user to enter a whole number
# it then calculates the factorial of that number

import random

def main():

    # Get the user input as a string
    user_input_string = input("Enter a whole number: ")
    print("")
    
    
    min = 1
    max = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print ("Rolling the dices...")
        print ("The values are....")
        print (random.randint(min, max))
        print (random.randint(min, max))

        roll_again = input("Roll the dices again?")
        
        
    try:
        # get the user number


    except Exception:
        print("That is not a number!!")



if __name__ == "__main__":
    main()
