from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
--------------------------
When you finish writing code in this file, StoneMasonKarel should
solve the  "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    """
    Repair each column, moving 4 steps in between. To repair a column,
    turn left and move until front_is_blocked, placing a beeper if there isn't
    one.

    Pre-condition: Karel is on the southwest-most corner, facing east.

    Post-condition: Karel is on the southeast-most corner, facing east.
    """
    repair_column()
    while front_is_clear():
        move_to_next_column()
        repair_column()

def move_to_next_column():
    for i in range(4):
        move()

def repair_column():
    """
    Repair one column and return to the same position.

    Pre-condition: Karel is facing east at the base of a column.

    Post-condition: Karel is in the same position and orientation as start.
    """
    turn_left()
    fill_column()
    return_to_ground()
    turn_left()

def fill_column():
    """
    Fill every spot in a column that is missing a beeper.

    Pre-condition: Karel is facing north at the base of a column.

    Post-condition: Karel is facing north at the top of a column.
    """
    fill_corner()
    while front_is_clear():
        move()
        fill_corner()

def return_to_ground():
    """
    Return to the base of a column.

    Pre-condition: Karel is facing north at the top of a column.

    Post-condition: Karel is facing south at the base of a column.
    """
    turn_around()
    while front_is_clear():
        move()

def fill_corner():
    if no_beepers_present():
        put_beeper()

def turn_around():
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
