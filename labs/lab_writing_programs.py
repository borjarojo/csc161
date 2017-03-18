"""CSC 161 Lab: Writing Programs

This program implements a basic interactive calculator.

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""


def main():
    print("This program evaluates arithmetic expresions!")
    n = eval(input("How many calculations would you like to make? "))
    for i in range(n):  # Changed from 100 to the input 'n' for extra credit
        x = input("Enter a mathematical expression: ")
        print(x, "=", eval(x))

main()
