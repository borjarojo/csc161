"""CSC 161 Project

This program:

Reads in stock data from Apple and can look up certain stock values

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""

from Data import Data
from Account import Account
from Analysis import Analysis


def main():
    alg_moving_average = Analysis(Data(), Account())
    alg_moving_average.alg_moving_average()

    alg_mine = Analysis(Data(), Account())
    alg_mine.alg_mine()

    print("Result for moving average algorithm:", alg_moving_average)
    print("Result for my algorithm:", alg_mine)

if __name__ == '__main__':
    main()