from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------------------
When you finish writing this file, TripleKarel should be
able to pain the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    """
    Paint each building, one wall at a time, by turning left in between each
    of three walls and turning right in between each of 3 buildings.
    """
    paint_building()
    for i in range(2):
        turn_right()
        paint_building()

def paint_building():
    paint_wall()
    for i in range(2):
        turn_left()
        move()
        paint_wall()

def paint_wall():
    while left_is_blocked():
        put_beeper()
        move()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
