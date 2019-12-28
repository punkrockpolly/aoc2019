from collections import defaultdict


DAY_24_INPUT = """####.
.###.
.#..#
##.##
###.."""

TEST_INPUT = ("""....#
#..#.
#..##
..#..
#....""", 2129920)


def parse_input(puzzle_input):
    discord_list = []
    neighbors = defaultdict(list)
    lines = puzzle_input.splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            discord_list.append(char)
            current_pos = len(discord_list) - 1
            if y + 1 < len(lines):
                neighbors[current_pos].append(x + (len(line) * (y + 1)))
            if y - 1 >= 0:
                neighbors[current_pos].append(x + (len(line) * (y - 1)))
            if x + 1 < len(line):
                neighbors[current_pos].append(x + 1 + (len(line) * y))
            if x - 1 >= 0:
                neighbors[current_pos].append(x - 1 + (len(line) * y))

    return discord_list, neighbors


def grow_bugs(current_state, neighbors, seen):
    while True:
        new_state = []
        for i, s in enumerate(current_state):
            adjacent = neighbors[i]
            if s == '#':
                if sum(current_state[n] == '#' for n in adjacent) == 1:
                    new_state.append('#')
                else:
                    new_state.append('.')
            elif s == '.':
                if sum(current_state[n] == '#' for n in adjacent) in (1, 2):
                    new_state.append('#')
                else:
                    new_state.append('.')
        current_state = ''.join(new_state)
        if current_state in seen:
            return current_state
        seen.add(current_state)


def biodiversity(current_state):
    total = 0
    for i, s in enumerate(current_state):
        total += 2**i if s == '#' else 0
    return total


def discord(puzzle_input):
    discord_list, neighbors = parse_input(puzzle_input)
    current_state = ''.join(discord_list)
    seen = {current_state}
    repeat_state = grow_bugs(current_state, neighbors, seen)
    return biodiversity(repeat_state)


test_in, test_out = TEST_INPUT
print(test_in)
output = discord(test_in)
print("expected: ", test_out)
print("output: ", output)
assert output == test_out


print(discord(DAY_24_INPUT))
