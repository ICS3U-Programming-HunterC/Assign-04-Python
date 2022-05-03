#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 21, 2022
# This program rolls a dice and if they roll a
# double they win

import random


def main():
    # initialize min, max and the counter
    min = 1
    max = 6
    counter = 0

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        counter = counter + 1
        # generate 2 random numbers
        random_1 = random.randint(min, max)
        random_2 = random.randint(min, max)
        # display the dice rolled
        print("Rolling the dice...")
        print("The values are....")
        print(random_1, end=" ")
        print(random_2)
        print("")

        # if the dice are the same, then it will roll doubles and the
        # program will end and tell them how many attempts it took
        if random_1 == random_2:
            print("You rolled doubles!! Thanks for playing!")
            print("It took {0} attempts to roll doubles".format(counter))
            roll_again = input("Do you want to play again?: ")
            print("")
            # once they roll doubles, the program will ask if the want to
            # roll again, if they enter yes it will, if not it will end
            if roll_again == "yes" or roll_again == "y":
                counter = 0
                continue
            else:
                print("Thanks for playing!!")
                break

        # ask the user if they want to roll again
        roll_again = input("Roll the dices again?: ")

        # if they input no, the program will end
        if roll_again == "no" or roll_again == "n":
            print("Thanks for playing!!")
            break


if __name__ == "__main__":
    main()
