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

TEST_INPUTS = [(""".#..#
.....
#####
....#
...##
""", 8),
("""......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
""", 33),
("""#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
""", 35),
(""".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
""", 41),
(""".#..##.###...#######
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
""", 210)]


def find_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    numerator = y1 - y2
    direction_n = numerator / abs(numerator) if numerator != 0 else 0
    denominator = x1 - x2
    direction_d = denominator / abs(denominator) if denominator != 0 else 0
    if denominator == 0:
        return (direction_n, "-infinity")
    if numerator == 0:
        return (direction_d, "infinity")
    return (direction_n, numerator / denominator)


def parse_input(astroids_input):
    astroids_set = set()
    lines = astroids_input.splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                astroids_set.add((x, y))

    return astroids_set


def find_location(puzzle_input):
    astroids_set = parse_input(puzzle_input)
    max_astroids = 0

    for astroid1 in astroids_set:
        astroid_slopes = set()
        for astroid2 in astroids_set:
            if astroid1 == astroid2:
                continue
            slope = find_slope(astroid1, astroid2)
            astroid_slopes.add(slope)
        count = len(astroid_slopes)
        if count > max_astroids:
            max_astroids = count

    return max_astroids


for (test_in, test_out) in TEST_INPUTS:
    print(test_in)
    output = find_location(test_in)
    print("output: ", output)
    assert output == test_out


print(find_location(DAY_10_INPUT))
