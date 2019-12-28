DAY_2_INPUT = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 6, 19, 23, 2, 23,
               6, 27, 1, 5, 27, 31, 1, 31, 9, 35, 2, 10, 35, 39, 1, 5, 39, 43, 2, 43, 10, 47, 1,
               47, 6, 51, 2, 51, 6, 55, 2, 55, 13, 59, 2, 6, 59, 63, 1, 63, 5, 67, 1, 6, 67, 71, 2,
               71, 9, 75, 1, 6, 75, 79, 2, 13, 79, 83, 1, 9, 83, 87, 1, 87, 13, 91, 2, 91, 10, 95,
               1, 6, 95, 99, 1, 99, 13, 103, 1, 13, 103, 107, 2, 107, 10, 111, 1, 9, 111, 115, 1,
               115, 10, 119, 1, 5, 119, 123, 1, 6, 123, 127, 1, 10, 127, 131, 1, 2, 131, 135, 1,
               135, 10, 0, 99, 2, 14, 0, 0]

TEST_INPUTS = [
    ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]),
    ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])
]


def gravity_assist(puzzle_input):
    output = puzzle_input.copy()
    length = len(puzzle_input)

    for n in range(0, length, 4):
        opcode = output[n]
        if opcode == 99:
            return output
        pos_one = output[n + 1]
        pos_two = output[n + 2]
        pos_three = output[n + 3]

        if opcode == 1:
            output[pos_three] = output[pos_one] + output[pos_two]
        elif opcode == 2:
            output[pos_three] = output[pos_one] * output[pos_two]
        else:
            print("ERROR")

for (test_in, test_out) in TEST_INPUTS:
    assert gravity_assist(test_in) == test_out

print(gravity_assist(DAY_2_INPUT)[0])
