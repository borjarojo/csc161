"""CSC 161 Lab: Decision Control

This program demonstrates the use of 'if' statements.

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""

# I'm not sure what the extra credit means by exception
# handling, but I do have the 400 and 100 year rule
# incorporated with my leap year funcion. My program
# should be able to handle any date.


def dateCheck(m, d, y):
    mmax = 12
    dmax = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Bool set
    validMonthAndDay = m >= 1 and m <= mmax and d >= 1 and d <= dmax[m - 1]
    validLeap = checkLeap(m, d, y)

    # Control statements
    if validMonthAndDay or validLeap:
        return True
    else:
        return False


def checkLeap(m, d, y):
    # 29th, Feb, a year divisible by 400 or one divisible by 4 but not 100
    if d == 29 and m == 2 and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        return True
    else:
        return False


def main():
    # Intro
    print("This program accepts a date in the form month/day/year\n"
          "and outputs whether or not the date is valid")

    # Querry
    date = input("Please enter a date (mm/dd/yyyy): ")
    m, d, y = [int(i) for i in date.split("/")]

    # Formated print
    print("{0}/{1}/{2} is {3} valid".format(
            m, d, y, "\b" if dateCheck(m, d, y) else "not"))

main()
