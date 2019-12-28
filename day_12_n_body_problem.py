DAY_12_INPUT = {
    'io': {'pos': {'x': -3, 'y': 15, 'z': -11}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
    'europa': {'pos': {'x': 3, 'y': 13, 'z': -19}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
    'ganymede': {'pos': {'x': -13, 'y': 18, 'z': -2}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
    'callisto': {'pos': {'x': 6, 'y': 0, 'z': -1}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
}

TEST_INPUTS = [
    ({
        'io': {'pos': {'x': -1, 'y': 0, 'z': 2}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
        'europa': {'pos': {'x': 2, 'y': -10, 'z': -7}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
        'ganymede': {'pos': {'x': 4, 'y': -8, 'z': 8}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
        'callisto': {'pos': {'x': 3, 'y': 5, 'z': -1}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
    }, 10, 179),
    ({
        'io': {'pos': {'x': -8, 'y': -10, 'z': 0}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
        'europa': {'pos': {'x': 5, 'y': 5, 'z': 10}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
        'ganymede': {'pos': {'x': 2, 'y': -7, 'z': 3}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
        'callisto': {'pos': {'x': 9, 'y': -8, 'z': -3}, 'vel': {'x': 0, 'y': 0, 'z': 0}},
    }, 100, 1940),
]


def update_velocity(moon1, moon2):
    for position in ['x', 'y', 'z']:
        p1 = moon1['pos'][position]
        p2 = moon2['pos'][position]

        if p1 > p2:
            moon1['vel'][position] -= 1
            moon2['vel'][position] += 1
        elif p1 < p2:
            moon1['vel'][position] += 1
            moon2['vel'][position] -= 1


def update_position(moon):
    for position in ['x', 'y', 'z']:
        moon['pos'][position] += moon['vel'][position]


def calculate_total_energy(moon):
    potential_energy = sum([abs(pos) for pos in moon['pos'].values()])
    kinetic_energy = sum([abs(pos) for pos in moon['vel'].values()])

    return potential_energy * kinetic_energy


def make_moves(puzzle_data, steps):
    for i in range(steps):
        done = []
        for moon1 in puzzle_data:
            done.append(moon1)
            for moon2 in puzzle_data:
                if moon2 in done:
                    continue
                update_velocity(puzzle_data[moon1], puzzle_data[moon2])

        for moon in puzzle_data:
            update_position(puzzle_data[moon])

    return sum([calculate_total_energy(puzzle_data[moon]) for moon in puzzle_data])


for (test_in, steps, test_out) in TEST_INPUTS:
    print(test_in)
    output = make_moves(test_in, steps)
    print("output: ", output)
    assert output == test_out

print(make_moves(DAY_12_INPUT, 1000))
