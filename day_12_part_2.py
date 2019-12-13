import copy
import itertools


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


def update_velocity(moon1, moon2):
    for position in range(3):
        p1 = moon1[position]
        p2 = moon2[position]

        if p1 > p2:
            moon1[position + 3] -= 1
            moon2[position + 3] += 1
        elif p1 < p2:
            moon1[position + 3] += 1
            moon2[position + 3] -= 1


def update_position(moon):
    for position in range(3):
        moon[position] += moon[position + 3]


def make_moves(puzzle_data):
    starting_data = copy.deepcopy(puzzle_data)
    i = 0

    while True:
        i += 1
        for moon1, moon2 in itertools.combinations(range(4), 2):
            update_velocity(puzzle_data[moon1], puzzle_data[moon2])

        for moon in range(4):
            update_position(puzzle_data[moon])

        if puzzle_data == starting_data:
            break

    return i


for (test_in, test_out) in TEST_INPUTS:
    print(test_in)
    output = make_moves(test_in)
    print("output: ", output)
    assert output == test_out

print(make_moves(DAY_12_INPUT))
