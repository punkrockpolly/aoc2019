from collections import defaultdict


DAY_24_INPUT = ("""####.
.###.
.#..#
##.##
###..""", 200)

TEST_INPUT = ("""....#
#..#.
#.?##
..#..
#....""", 10, 99)


def parse_input(puzzle_input):
    """Parse the initial state to build state array and neighbors map."""
    discord_list = []
    neighbors = defaultdict(list)
    lines = puzzle_input.splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            discord_list.append(char)
            current_pos = (0, x + (len(line) * y))
            if current_pos[1] == 12:  # we don't talk about tile 12
                continue
            if y == 0:
                neighbors[current_pos].append((-1, 7))
            if y + 1 < len(lines):
                neighbors[current_pos].append((0, x + (len(line) * (y + 1))))
            if y - 1 >= 0:
                neighbors[current_pos].append((0, x + (len(line) * (y - 1))))
            if y == len(lines) - 1:
                neighbors[current_pos].append((-1, 17))
            if x == 0:
                neighbors[current_pos].append((-1, 11))
            if x + 1 < len(line):
                neighbors[current_pos].append((0, x + 1 + (len(line) * y)))
            if x - 1 >= 0:
                neighbors[current_pos].append((0, x - 1 + (len(line) * y)))
            if x == len(line) - 1:
                neighbors[current_pos].append((-1, 13))
            if current_pos[1] == 7:
                neighbors[current_pos].extend([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)])
                neighbors[current_pos].remove((0, 12))
            elif current_pos[1] == 11:
                neighbors[current_pos].extend([(1, 0), (1, 5), (1, 10), (1, 15), (1, 20)])
                neighbors[current_pos].remove((0, 12))
            elif current_pos[1] == 13:
                neighbors[current_pos].extend([(1, 4), (1, 9), (1, 14), (1, 19), (1, 24)])
                neighbors[current_pos].remove((0, 12))
            elif current_pos[1] == 17:
                neighbors[current_pos].extend([(1, 20), (1, 21), (1, 22), (1, 23), (1, 24)])
                neighbors[current_pos].remove((0, 12))
    return discord_list, neighbors


def get_neighbors(current_pos, neighbors):
    """Return all neighbors, adjusting for level."""
    current_level, i = current_pos
    adjacent = neighbors[(0, i)]
    return [(current_level + level, position) for (level, position) in adjacent]


def grow_bugs_n_minutes(tiles, neighbors, minutes):
    """Grow bugs in a loop."""
    for ts in range(minutes):
        # add new level if edge level has life
        max_lvl = max(tiles)
        min_lvl = min(tiles)
        new_state = '.........................'
        if '#' in tiles[max_lvl]:
            tiles[max_lvl + 1] = new_state
        if '#' in tiles[min_lvl]:
            tiles[min_lvl - 1] = new_state
        tiles = grow_bugs_one_minute(tiles, neighbors)
    return tiles


def grow_bugs_one_minute(tiles, neighbors):
    """One iteration of growth."""
    end_state = {}
    for level, current_state in tiles.items():
        new_state = []
        for i, s in enumerate(current_state):
            if i == 12:  # we don't talk about tile 12
                new_state.append('?')
                continue
            adjacent = get_neighbors((level, i), neighbors)
            if s == '#':
                # A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
                if count_adjacent_bugs(tiles, adjacent) == 1:
                    new_state.append('#')
                else:
                    new_state.append('.')
            elif s == '.':
                # An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
                if count_adjacent_bugs(tiles, adjacent) in (1, 2):
                    new_state.append('#')
                else:
                    new_state.append('.')
            current_state = ''.join(new_state)
            end_state[level] = current_state
    return end_state


def count_adjacent_bugs(tiles, adjacent):
    return sum(tiles[lvl][n] == '#' for (lvl, n) in adjacent if lvl in tiles)


def count_total_bugs(end_state):
    return sum([char == '#' for tile in end_state.values() for char in tile])


def discord(puzzle_input, minutes):
    """Main function."""
    discord_list, neighbors = parse_input(puzzle_input)
    current_state = ''.join(discord_list)
    tiles = {0: current_state}
    end_state = grow_bugs_n_minutes(tiles, neighbors, minutes)
    total_bugs = count_total_bugs(end_state)
    return total_bugs


test_in, minutes, test_out = TEST_INPUT
print(test_in)
output = discord(test_in, minutes)
print("expected: ", test_out)
print("output: ", output)
assert output == test_out


print(discord(*DAY_24_INPUT))
