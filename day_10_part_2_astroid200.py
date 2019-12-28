from collections import defaultdict
from math import atan2, degrees


DAY_10_INPUT = """###..#.##.####.##..###.#.#..
#..#..###..#.......####.....
#.###.#.##..###.##..#.###.#.
..#.##..##...#.#.###.##.####
.#.##..####...####.###.##...
##...###.#.##.##..###..#..#.
.##..###...#....###.....##.#
#..##...#..#.##..####.....#.
.#..#.######.#..#..####....#
#.##.##......#..#..####.##..
##...#....#.#.##.#..#...##.#
##.####.###...#.##........##
......##.....#.###.##.#.#..#
.###..#####.#..#...#...#.###
..##.###..##.#.##.#.##......
......##.#.#....#..##.#.####
...##..#.#.#.....##.###...##
.#.#..#.#....##..##.#..#.#..
...#..###..##.####.#...#..##
#.#......#.#..##..#...#.#..#
..#.##.#......#.##...#..#.##
#.##..#....#...#.##..#..#..#
#..#.#.#.##..#..#.#.#...##..
.#...#.........#..#....#.#.#
..####.#..#..##.####.#.##.##
.#.######......##..#.#.##.#.
.#....####....###.#.#.#.####
....####...##.#.#...#..#.##.
"""

TEST_INPUTS = [(""".#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##
""", 9, (8, 3), (15, 1)), (""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""", 200, (11, 13), (8, 2)), ]


def find_degrees(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    y = y2 - y1
    x = x2 - x1

    degree = degrees(atan2(y, x)) + 90
    degree = (degree + 360) % 360
    return degree


def parse_input(astroids_input):
    astroids_set = set()
    lines = astroids_input.splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                astroids_set.add((x, y))

    return astroids_set


def find_nth(puzzle_input, astroid1, n):
    astroids_set = parse_input(puzzle_input)
    destroyed_astroids = 0
    degrees_map = defaultdict(list)
    for astroid2 in astroids_set:
        if astroid1 == astroid2:
            continue
        degree = find_degrees(astroid1, astroid2)
        degrees_map[degree].append(astroid2)

    for degree in sorted(degrees_map):
        astroids = degrees_map[degree]
        # print(destroyed_astroids + 1, degree, astroids)
        if len(astroids) == 1:
            astroid = astroids[0]
            del degrees_map[degree]
        else:
            astroid = degrees_map[degree].pop()
        destroyed_astroids += 1
        if destroyed_astroids == n:
            return astroid


for (test_in, n, location, test_out) in TEST_INPUTS:
    # print(test_in)
    output = find_nth(test_in, location, n)
    # print("output: ", output)
    assert output == test_out


astroid200 = find_nth(DAY_10_INPUT, (22, 19), 200)
x, y = astroid200
print(100 * x + y)
