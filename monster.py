from collections import namedtuple
import math

BASE_HP = 1
BASE_HEARING = 10
BASE_DAMAGE = 1


def monster_dead(monster):
    """ Returns true if a monster is dead, that is their hp is less than or equal to zero.

    Examples:
    >>> monster_dead((0, 1, 1))
    True
    >>> monster_dead((10, 1, 1))
    False
    """
    (hp, _, _) = monster
    return hp <= 0


def new_monster():
    """ Return a new monster based on the default damage, hp, and hearing values.

    Examples:
    >>> new_monster()
    (1, 10, 1)
    """
    return (BASE_HP, BASE_HEARING, BASE_DAMAGE)


def monster_can_hear(monster, monster_x, monster_y, target_x, target_y):
    """ Returns True if a monster at x, y can hear what's going on at target_x, target_y.
    Examples:
    >>> monster_can_hear(new_monster(), 0, 0, 5, 5)
    True
    >>> monster_can_hear(new_monster(), 0, 0, 10, 11)
    False
    """
    (_, hearing, _) = monster
    dist = abs(monster_x - target_x) + abs(monster_y - target_y)
    return dist <= hearing


def monster_inflict_damage(player, monster):
    """ Inflicts damage on a player according to a monsters damage stat and returns a new player.

    Examples:
    >>> player = (0, 0, 10, 1)
    >>> monster_inflict_damage(player, new_monster)
    (0, 0, 9, 1) """
    x, y, hp, p_damage = player
    _, _, damage = monster
    return (x, y, hp - damage, p_damage)


def monster_path(monster_x, monster_y, target_x, target_y):
    """ Attempt to path (simply) from current position to some other target_x and target_y on the level.

    Pathing algorithm is as follows:
    - If we are to the right of the target move left
    - If we are to the left of the target move right
    - If we are above the target move down
    - If we are below the target move up

    NOTE: does not take into account walls or obstacles. The ambitious and brave
    may use something like Djikstra's or A* to compute the shortest path taking
    into account these obstacles.

    Returns:
    The direction the monster should move in to head towards the target.

    Examples:
    >>> monster_path(0, 0, 10, 10)
    (1, 1)
    >>> monster_path(0, 0, 2, 0)
    (1, 0)
    >>> monster_path(0, 0, 0, 2)
    (0, 1)
    >>> monster_path(0, 0, 0, 0)
    (0, 0) """
    if target_x == monster_x:
        x_direction = 0
    elif target_y == monster_y:
        y_direction = 0
    return x_direction, y_direction
