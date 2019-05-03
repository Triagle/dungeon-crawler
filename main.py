#!/usr/bin/env python

import level as l
import monster as m
import player as p
import random
import tty
import sys
import termios

QUIT = 0
MOVE = 1
MAX_X = 60
MAX_Y = 30
TILES = {l.WALL: "#", l.FLOOR: "."}
PLAYER = "@"
MONSTER = "x"


def perform_player_action(level, player, monsters, action):
    """ Execute a given action, updating the level, player and monsters to reflect changes occurring as effects of the player's actions. """
    #######################
    # YOUR CODE GOES HERE #
    #######################
    pass


def clean_up_monsters(monsters):
    """ Remove a new set of monsters containing only those that aren't currently dead. """
    return {
        p: monster for p, monster in monsters.items() if not m.monster_dead(monster)
    }


def move_monsters(level, player, monsters):
    """ Move all monsters on the level, attacking the player if allowed to do so. """
    #######################
    # YOUR CODE GOES HERE #
    #######################
    pass


def draw_level(level, player, monsters):
    """ Draw the current level, as well as the players and the monsters in the level to the console. """
    #######################
    # YOUR CODE GOES HERE #
    #######################
    pass


def clear_screen():
    """ Clear the terminal screen. """
    print("\x1bc")


def read_player_input():
    """ Read a player's input into an action, either quit or move in a given direction. """
    c = sys.stdin.read(1)[0]
    if c == "q":
        return QUIT
    elif c == "a":
        return (MOVE, -1, 0)
    elif c == "d":
        return (MOVE, 1, 0)
    elif c == "s":
        return (MOVE, 0, 1)
    elif c == "w":
        return (MOVE, 0, -1)
    else:
        return None


def main():
    # Set linux terminal input mode to allow character level input
    tty_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    level, player, monsters = l.load_level("level.txt")
    draw_level(level, player, monsters)
    while True:
        action = read_player_input()
        if action == QUIT:
            break
        elif action is not None:
            #######################
            # YOUR CODE GOES HERE #
            #######################
            pass
        if p.is_dead(player):
            print("You lose!")
            break

        draw_level(level, player, monsters)

    # restore linux terminal settings
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, tty_settings)


if __name__ == "__main__":
    main()
