import player
import monster

# Level tile types
WALL = 1
FLOOR = 2


def load_level(filename):
    """ Parse a level from a filename pointing to a level text file.

    Levels are ascii text files drawing one for one the layout of the dungeon
    with characters exactly matching those in the game. Returns a level
    containing a dictionary with keys (x, y) coordinates and values the kind of
    tile at this position (WALL or FLOOR). Also returns the player, and a
    dictionary with keys (x, y) and values monsters spawned at a given position.

    Example Level:

    #######
    #.@........             ####################
    #.....#   x             #..............#..x#
    #######   .             #..................#
              .             #..............#####
            ##.###          #..............#..x#
            #..................................#
            ######          #..............#####
                            #..............#..x#
                            #..................#
                            #..............#####
                            #..............#..x#
                            #..................#
                            #..............#####
                            #..............#..x#
                            #..................#
                            ####################

    - The @ and x signs are spawn positions for player and monster respectively.
    - "." denotes the floor.
    - "#" denotes the wall. """
    level = {}
    monsters = {}
    p = None
    with open(filename, "r") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                if c == ".":
                    level[(x, y)] = FLOOR
                elif c == "#":
                    level[(x, y)] = WALL
                elif c == "x":
                    monsters[(x, y)] = monster.new_monster()
                    level[(x, y)] = FLOOR
                elif c == "@":
                    p = player.new_player(x, y)
                    level[(x, y)] = FLOOR

        return level, p, monsters


def level_is_occupied(level, x, y):
    """ Return True if the point at (x, y) is able to be moved to. """
    #######################
    # YOUR CODE GOES HERE #
    #######################
    pass
