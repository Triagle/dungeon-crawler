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
    action_type = action[0]
    x, y = p.player_position(player)
    damage = p.player_damage(player)
    health = p.player_hp(player)
    if action_type == QUIT:
        return level, player, monsters, True
    elif action_type == MOVE:
        _, x_direction, y_direction = action
        new_x, new_y = x + x_direction, y + y_direction
        if l.level_is_occupied(level, new_x, new_y):
            return level, player, monsters, False
        elif (new_x, new_y) in monsters:
            monsters[(new_x, new_y)] = p.player_inflict_damage(
                player, monsters[(new_x, new_y)]
            )
            return level, player, monsters, False
        else:
            player = (new_x, new_y, health, p.player_damage(player))
            return level, player, monsters, False


def clean_up_monsters(monsters):
    """ Return a new set of monsters containing only those that aren't currently dead. """
    return {
        p: monster for p, monster in monsters.items() if not m.monster_dead(monster)
    }


def move_monsters(level, player, monsters):
    """ Move all monsters on the level, attacking the player if allowed to do so. """
    x, y, health, p_damage = player
    new_monsters = {}
    for (m_x, m_y), monster in monsters.items():
        if not m.monster_can_hear(monster, m_x, m_y, x, y):
            new_monsters[(m_x, m_y)] = monster
            continue

        x_dir, y_dir = m.monster_path(m_x, m_y, x, y)
        new_x, new_y = m_x + x_dir, m_y + y_dir
        if l.level_is_occupied(level, new_x, m_y):
            new_x = m_x
        if l.level_is_occupied(level, m_x, new_y):
            new_y = m_y
        if l.level_is_occupied(level, new_x, new_y):
            new_monsters[(m_x, m_y)] = monster
        elif x == new_x and y == new_y:
            player = m.monster_inflict_damage(player, monster)
            new_monsters[(m_x, m_y)] = monster
        else:
            new_monsters[(new_x, new_y)] = monster
    return level, player, new_monsters


def draw_level(level, player, monsters):
    """ Draw the current level, as well as the players and the monsters in the level to the console. """
    p_x, p_y = p.player_position(player)
    hp = p.player_hp(player)
    clear_screen()
    print(f"HP: {hp}")
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if x == p_x and y == p_y:
                print(PLAYER, end="")
            elif (x, y) in monsters:
                print(MONSTER, end="")
            elif (x, y) in level:
                print(TILES[level[(x, y)]], end="")
            else:
                print(" ", end="")
        print("")


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
            level, player, monsters, should_quit = perform_player_action(
                level, player, monsters, action
            )
            if should_quit:
                break
            level, player, monsters = move_monsters(
                level, player, clean_up_monsters(monsters)
            )
        if p.is_dead(player):
            print("You lose!")
            break

        draw_level(level, player, monsters)

    # restore linux terminal settings
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, tty_settings)


if __name__ == "__main__":
    main()
