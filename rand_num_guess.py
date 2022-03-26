#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: March 23, 2022
# This program asks the user for a random number 0-9
# then if check if they guessed it right or wrong
# and tell them the right number

# import math random
import random

# set random number between 0-9
random_number = random.randint(0, 9)


def main():
    # ask user for a number between 1-9
    guess_number = int(input("Enter a number between 0-9 "))
    print("")

    # check if the guessed the right number
    if guess_number == random_number:
        print("You guessed it right!")
    else:
        # display the right number if they guessed it wrong
        print("You guessed it wrong")
        print("The right number was ", random_number)


if __name__ == "__main__":
    main()
