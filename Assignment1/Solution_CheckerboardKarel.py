from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    """
    Place one row, then while Karel hasn't reached the top row,
    keep placing new rows by moving and placing beepers every other
    corner.
    """
    place_row()
    while not_top_row():
        go_to_next_row()
        place_row()

def place_row():
    move()
    while front_is_clear():
        put_beeper()
        move()
        move()
    put_beeper()

def go_to_next_row():
    if facing_east():
        turn_left()
        move()
        turn_left()
    else:
        turn_right()
        move()
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def not_top_row():
    return ((facing_east() and left_is_clear()) or
        (facing_west() and right_is_clear()))

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
