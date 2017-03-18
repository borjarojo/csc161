"""CSC 161 Lab: Data Collections

This lab runs a statistical analysis on a set of randomly
generated cards.

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""

from random import randrange, choice
from lab_class_design import PlayingCard
from math import sqrt

suit_size = 13  # Number of cards in a suit.
deck_size = 52  # Number of cards in a deck.
num_cards = 260  # Number of cards to create with random rank & suit values


def make_random_cards():
    """Generate num_cards number of random PlayingCard objects.

    This function will generate num_cards RANDOM playing cards
    using your PlayingCard class. That means you will have to choose a random
    suit and rank for a card num_cards times.

    Printing:
        Nothing

    Positional arguments:
        None

    Returns:
        cards_list -- a list of PlayingCard objects.
    """

    cards_list = []
    for i in range(num_cards):
        card = PlayingCard(randrange(1, 14), choice("schd"))
        cards_list.append(card)

    return cards_list


def freq_count(cards_list):
    """Count every suit-rank combination.

    Returns a dictionary whose keys are the card suit-rank and value is the
    count.

    Printing:
        Nothing

    Positional arguments:
        cards_list -- A list of PlayingCard objects.

    Returns:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'd', 'c', 'h', 's' representing each card suit.  The value for each key
        is a list containing the number of cards at each rank, using the index
        position to represent the rank. For example, {'s': [0, 3, 4, 2, 5]}
        says that the key 's', for 'spades' has three rank 1's (aces), four
        rank 2's (twos), two rank 3's (threes) and 5 rank 4's (fours).  Index
        position 0 is 0 since no cards have a rank 0, so make note.
    """
    # DO NOT REMOVE BELOW
    if type(cards_list) != list or \
            list(filter(lambda x: type(x) != PlayingCard, cards_list)):
        raise TypeError("cards_list is required to be a list of PlayingCard \
                        objects.")
    # DO NOT REMOVE ABOVE

    # Set up dictionary
    card_freqs = {'d': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  'c': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  'h': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  's': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

    # For every card in card_list, add 1 to the frequency of the suit-rank
    for card in cards_list:
        card_freqs[card.get_suit()][card.get_rank()] += 1

    return card_freqs


def std_dev(counts):
    """Calculate the standard deviation of a list of numbers.

    Positional arguments:
        counts -- A list of ints representing frequency counts.

    Printing:
        Nothing

    Returns:
        _stdev -- The standard deviation as a single float value.
    """
    # DO NOT REMOVE BELOW
    if type(counts) != list or \
            list(filter(lambda x: type(x) != int, counts)):
        raise TypeError("counts is required to be a list of int values.")
    # DO NOT REMOVE ABOVE

    # Find mean
    mean = 0
    for num in counts:
        mean += num
    mean /= len(counts)

    # Sum squares of distances to mean
    mean_dist_square_sum = 0
    for num in counts:
        mean_dist_square_sum += (num - mean)**2

    # Sqrt the average of the sums
    _stdev = sqrt(mean_dist_square_sum / len(counts))

    return _stdev


def print_stats(card_freqs):
    """Print the final stats of the PlayingCard objects.

    Positional arguments:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'dchs' representing each card suit. The value for each key is a list of
        numbers where each index position is a card rank, and its value is its
        card frequency.

        You will probably want to call th std_dev function in somewhere in
        here.

    Printing:
        Prints the statistic for each suit to the screen, see assignment page
        for an example output.

    Returns:
        None
    """
    # DO NOT REMOVE BELOW
    if type(card_freqs) != dict or \
            list(filter(lambda x: type(card_freqs[x]) != list, card_freqs)):
        raise TypeError("card_freqs is required to be a list of int values.")
    # DO NOT REMOVE ABOVE

    # Dictionary to convert suit key to name
    suit_name = {'d': 'Diamonds', 'h': 'Hearts', 's': 'Spades', 'c': 'Clubs'}

    # Printing
    print("Standard deviation for the frequency counts of each rank in suit:")
    for suit in card_freqs:
        print("\t" + suit_name[suit] + ":",
              std_dev(card_freqs[suit]),
              "cards")


def main():
    cards = make_random_cards()
    suit_counts = freq_count(cards)
    print_stats(suit_counts)


if __name__ == "__main__":
    main()
