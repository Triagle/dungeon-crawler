#!/usr/bin/env python

BASE_HEALTH = 10
BASE_DAMAGE = 1


def new_player(x, y):
    """ Return a new player at x, y based on stats.

    Examples:
    >>> new_player(0, 0)
    (0, 0, 10, 1)
    """
    return (x, y, BASE_HEALTH, BASE_DAMAGE)


def player_inflict_damage(player, monster):
    """ Inflict damage on monster according to the player's damage stat.

    Examples:
    >>> player_inflict_damage(new_player(0, 0), new_monster())
    (0, 10, 1) """
    _, _, _, damage = player
    hp, hear, m_damage = monster
    return (hp - damage, hear, m_damage)


def player_position(player):
    """ Return the player's current position.

    Examples:
    >>> player_position(new_player(10, 10))
    (10, 10) """
    x, y, _, _ = player
    return x, y


def player_hp(player):
    """ Return the player's current hp.

    Examples:
    >>> player_hp(new_player(0, 0))
    10
     """
    return player[2]


def player_damage(player):
    """ Return the player's current damage.

    Examples:
    >>> player_damage(new_player())
    1 """
    return player[3]


def is_dead(player):
    _, _, hp, _ = player
    return hp <= 0
