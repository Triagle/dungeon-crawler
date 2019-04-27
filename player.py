#!/usr/bin/env python

BASE_HEALTH = 10
BASE_DAMAGE = 1


def new_player(x, y):
    return (x, y, BASE_HEALTH, BASE_DAMAGE)


def player_inflict_damage(player, monster):
    _, _, _, damage = player
    hp, hear, m_damage = monster
    return (hp - damage, hear, m_damage)


def is_dead(player):
    _, _, hp, _ = player
    return hp <= 0
