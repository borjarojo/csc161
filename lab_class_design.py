"""CSC161: Class Design

This lab exemplifies the creation of classes in Python using
playng cards.

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""

import random

# Playing Card Class
class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def get_rank(self):
        return self.rank
    

    def get_suit(self):
        return self.suit


    def bj_value(self): 
        if self.rank > 10:
            return 10
        return self.rank


    # Converts the int rank into a string
    def str_rank(self):
        if self.rank == 1:
            return "Ace"
        elif self.rank == 2:
            return "Two"
        elif self.rank == 3:
            return "Three"
        elif self.rank == 4:
            return "Four"
        elif self.rank == 5:
            return "Five"
        elif self.rank == 6:
            return "Six"
        elif self.rank == 7:
            return "Seven"
        elif self.rank == 8:
            return "Eight"
        elif self.rank == 9:
            return "Nine"
        elif self.rank == 10:
            return "Ten"
        elif self.rank == 11:
            return "Jack"
        elif self.rank == 12:
            return "Queen"
        elif self.rank == 13:
            return "King"


    # Converts the letter of suit into a more full string
    def str_suit(self):
        if self.suit == "s":
            return "Spades"
        elif self.suit == "c":
            return "Clubs"
        elif self.suit == "h":
            return "Hearts"
        elif self.suit == "d":
            return "Diamonds"

    # Uses the string convertion functions to create a __repr__ string
    def __repr__(self):
        return self.str_rank() + " of " + self.str_suit()

def num_to_suit(num):
    num = num % 4
    if num == 0:
        return "s"
    elif num == 1:
        return "c"
    elif num == 2:
        return "h"
    elif num == 3:
        return "d"


def main():
    print("Testing card class")
    
    card_count = eval(input("How many cards would you like to see? "))

    """EXTRA CREDIT: The one line solution with a string and a randrange
    can be improved with the choice() function. Other wise, the solution
    is putting "schd"[random.randrange(4)] as the argument for the suit
    in the initialization for a playing card.
    """
    for i in range(card_count):
        card = PlayingCard(random.randrange(1, 14), random.choice("schd"))
        print(card, "counts", card.bj_value())


if __name__ == '__main__':
    main()

