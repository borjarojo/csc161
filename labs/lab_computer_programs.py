"""CSC 161 Lab: Computers and Programs

This program demonstrates the output of a chaotic function.

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""
# File: chaos.py
# A simple program illistration chaotic behavior.


def main():
    print("This program illustrates a chaotic function")
    n = eval(input("How many numbers should I print? "))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

main()
