from collections import namedtuple
import math

BASE_HP = 1
BASE_HEARING = 10
BASE_DAMAGE = 1


def monster_dead(monster):
    (hp, _, _) = monster
    return hp <= 0


def new_monster():
    return (BASE_HP, BASE_HEARING, BASE_DAMAGE)


def monster_can_hear(monster, monster_x, monster_y, target_x, target_y):
    """ Returns True if a monster at x, y can hear what's going on at target_x, target_y. """
    (_, hearing, _) = monster
    dist = abs(monster_x - target_x) + abs(monster_y - target_y)
    return dist <= hearing


def monster_inflict_damage(player, monster):
    x, y, hp, p_damage = player
    _, _, damage = monster
    return (x, y, hp - damage, p_damage)


def monster_path(monster_x, monster_y, target_x, target_y):
    """ Attempt to path (simply) from current position to some other target_x and target_y on the level. """
    x_direction = int(math.copysign(1, target_x - monster_x))
    y_direction = int(math.copysign(1, target_y - monster_y))
    if target_x == monster_x:
        x_direction = 0
    elif target_y == monster_y:
        y_direction = 0
    return x_direction, y_direction
