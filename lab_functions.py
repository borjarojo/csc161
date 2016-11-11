"""CSC 161 Lab: Functions

The programs exemplifies the use of functions in Python.

Borja Rojo
Lab Section TR 2:00-3:15
Fall 2016
"""


import re


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def sumList(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def main():
    # Intro
    print("This programs exemplifies many different kinds of functions.")
    # Test squareEach
    numberList = [1, 2, 3, 4]
    print("\nnumberList before going through squareEach():", numberList)
    squareEach(numberList)
    print("numberList after going through squareEach()", numberList)

    # Test sumList
    toSum = [1000, 300, 30, 7]
    print("\ntoSum:", toSum)
    print("sumList(toSum):", sumList(toSum))  # Returns a summed list

    # Test toNumbers
    stringNumbers = ["40", "92", "77", "16"]
    print("\nstringNumbers type before toNumbers():", type(stringNumbers[0]))
    toNumbers(stringNumbers)
    print("stringNumbers type after toNumbers():", type(stringNumbers[0]))

    # Combo!!! (Can use either file)
    print("\nThis program will now attempt to use all three functions\n"
          "to convert a list of numbers in a file to the sum of thier\n"
          "squares.\n")

    fileName = input("File to be read: ")
    print("Openning file...")
    toRead = open(fileName, "r")
    print("Reading file...")
    readFile = toRead.readline()
    print("Closing file...")
    toRead.close()

    print("Seperating numbers in single-line file...")
    numbers = re.split(" |,", readFile)
    print("Converting strings into numbers...")
    toNumbers(numbers)
    print("Squaring all numbers...")
    squareEach(numbers)
    print("Adding up all numbers...")
    print("Result:", sumList(numbers))

main()
