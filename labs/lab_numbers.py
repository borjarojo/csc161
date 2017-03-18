"""CSC 161 Lab: Numbers

This program estimates square roots using Newton's Method

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""

# Some lines are longer than 80 characters.
# This was done to emulate the examples given.


import math


def main():
    # Intro
    print("This program calculates the square root"
          "of a given number using the Newton's method")

    # Querry
    number = eval(input("What is the number for which you want"
                        "to calculate the square root? "))
    count = eval(input("How many iterations do you want to use? "))

    # Estimation
    guess = number / 2
    for i in range(count):
        #     Loop#  Guess  Difference between guess and actual root
        guess = (guess + (number / guess)) / 2.0
        print(i + 1, guess, guess - math.sqrt(number))

    print("My guess for the square root of", number, "is", guess)
    print("The difference between my guess and the real result is",
          guess - math.sqrt(number))

main()
