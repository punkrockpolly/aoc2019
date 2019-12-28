from math import gcd


DAY_12_INPUT = [[-3, 15, -11, 0, 0, 0],
                [3, 13, -19, 0, 0, 0],
                [-13, 18, -2, 0, 0, 0],
                [6, 0, -1, 0, 0, 0],
                ]

TEST_INPUTS = [([[-1, 0, 2, 0, 0, 0],
                 [2, -10, -7, 0, 0, 0],
                 [4, -8, 8, 0, 0, 0],
                 [3, 5, -1, 0, 0, 0],
                 ], 2772),
               ]


def update_velocity(moon1, moon2, axis):
    p1 = moon1[axis]
    p2 = moon2[axis]

    if p1 > p2:
        moon1[axis + 3] -= 1
        moon2[axis + 3] += 1
    elif p1 < p2:
        moon1[axis + 3] += 1
        moon2[axis + 3] -= 1


def update_position(moon, axis):
    moon[axis] += moon[axis + 3]


def lcm(a, b):
    """Compute the lowest common multiple of a and b."""
    return a * b // gcd(a, b)


def make_moves(puzzle_data):
    starting = {axis: [row[axis] for row in puzzle_data] for axis in range(3)}
    combinations = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    period = {}

    for axis in range(3):
        i = 0
        while True:
            i += 1

            for moon1, moon2 in combinations:
                update_velocity(puzzle_data[moon1], puzzle_data[moon2], axis)

            for moon in range(4):
                update_position(puzzle_data[moon], axis)

            if (starting[axis] == [row[axis] for row in puzzle_data] and
                    [0, 0, 0, 0] == [row[axis + 3] for row in puzzle_data]):
                period[axis] = i
                break

    return lcm(period[0], lcm(period[1], period[2]))


for (test_in, test_out) in TEST_INPUTS:
    print(test_in)
    output = make_moves(test_in)
    print("output: ", output)
    assert output == test_out

print(make_moves(DAY_12_INPUT))
