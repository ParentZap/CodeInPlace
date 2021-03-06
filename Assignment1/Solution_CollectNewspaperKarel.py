from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Move Karel to the top right corner, then to the entrance, then out. Pick up
    the beeper and turn around, then move to the back middle of the house,
    then back to her corner, using a series of turn_left, turn_right and
    turn_around.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
