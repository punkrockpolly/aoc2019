DAY_1_INPUT = [
    113373,
    132031,
    104150,
    65914,
    81792,
    148723,
    94982,
    117511,
    89533,
    114335,
    128953,
    53970,
    52522,
    146264,
    89614,
    90375,
    114054,
    110582,
    91958,
    64811,
    58692,
    138427,
    81558,
    132987,
    138904,
    75785,
    99259,
    113640,
    84250,
    83134,
    80260,
    116018,
    76186,
    81457,
    107235,
    108657,
    98110,
    69048,
    63806,
    57223,
    65387,
    73452,
    80704,
    55250,
    116562,
    120546,
    145999,
    146063,
    100858,
    90460,
    72073,
    126926,
    131708,
    131592,
    104792,
    91527,
    128114,
    139831,
    99430,
    97397,
    129211,
    102181,
    118278,
    97812,
    119580,
    100912,
    66865,
    99460,
    128493,
    76092,
    139993,
    57749,
    83111,
    127747,
    101243,
    100619,
    79018,
    81946,
    146650,
    142257,
    139882,
    52795,
    76248,
    62824,
    137418,
    60898,
    108234,
    55589,
    132193,
    51191,
    56727,
    84285,
    131930,
    123750,
    62959,
    120799,
    86276,
    111156,
    124185,
    105008]

TEST_INPUTS = [
    ([14], 2),
    ([1969], 966),
]


def sum_fuel(mass):
    subtotal = int(mass / 3) - 2
    if subtotal <= 0:
        return 0
    else:
        return (subtotal + sum_fuel(subtotal))


def rocket_equation_part2(puzzle_input):
    total = 0
    for n in puzzle_input:
        subtotal = sum_fuel(n)
        total += subtotal

    return total


for (test_in, test_out) in TEST_INPUTS:
    output = rocket_equation_part2(test_in)
    assert output == test_out

print(rocket_equation_part2(DAY_1_INPUT))
