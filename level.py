import player
import monster

# Level tile types
WALL = 1
FLOOR = 2


def load_level(filename):
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
    return level.get((x, y)) == WALL or (x, y) not in level
