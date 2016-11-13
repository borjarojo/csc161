"""CSC 161 Lab: Simulation & Design

This lab helps estimate the expected distance a man would move from a
starting point with a random walk.

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""

import random

# Returns a list of ints from 0-3 which represent the 4 directions
# someone could walk in a grid pattern
def random_walk_2d(step_count):
    path = []
    
    # Generate random ints between 0 and 3 
    for i in range(step_count):
        path.append(random.randrange(0,4))
    
    return path


"""This funciton takes a path which is a list of numbers 0-3 and
calculates the distance from it's start point.

0 = up, 1 = right, 2 = down, 3 = left
"""
def distance_walked(path):
    # Distance Vars
    x_distance = 0
    y_distance = 0
    
    # Path eval
    for i in range(len(path)):
        if path[i] == 0:
            y_distance += 1
        elif path[i] == 1:
            x_distance += 1
        elif path[i] == 2:
            y_distance -= 1
        elif path[i] == 3:
            x_distance -= 1

    # Distance Eval
    distance = (x_distance ** 2 + y_distance ** 2)**(1 / 2)

    return distance

def average_walk_distance(walk_count, step_count):
    average_distance = 0

    # Calculate total
    for i in range(walk_count):
        average_distance += distance_walked(random_walk_2d(step_count))
    
    # Divide to get average
    average_distance /= walk_count

    return average_distance


def main():
    print("Simulation of two dimensional random walk")

    walks = eval(input("How many walks should I do? "))
    steps = eval(input("How many steps should I take on each? "))

    av_dist = average_walk_distance(walks, steps)
    print("Average distance from start:", av_dist)


if __name__ == '__main__':
    main()

