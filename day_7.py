from itertools import permutations


DAY_7_INPUT = [3,8,1001,8,10,8,105,1,0,0,21,46,55,68,89,110,191,272,353,434,99999,3,9,1002,9,3,9,1001,9,3,9,102,4,9,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,3,9,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,5,9,1002,9,2,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,102,3,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]  # noqa

TEST_INPUTS = [
    ([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], 43210),  # noqa
    ([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], 54321),  # noqa
    ([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], 65210),  # noqa
]


def interpret_opcode(opcode):
    opcode = '0000' + str(opcode)
    instruction = int(opcode[-2:])
    mode_1 = int(opcode[-3:][0])
    mode_2 = int(opcode[-4:][0])

    return (instruction, mode_1, mode_2)


def intcode(puzzle_data, phase_setting, input_signal):
    length = len(puzzle_data)
    n = 0
    output = "null"
    # print(puzzle_data)

    while n < length:
        (opcode, mode_1, mode_2) = interpret_opcode(puzzle_data[n])

        if opcode == 99:
            # print(puzzle_data)
            return output

        input_one = puzzle_data[n + 1]

        if opcode == 1:
            input_two = puzzle_data[n + 2]
            input_three = puzzle_data[n + 3]
            param_1 = puzzle_data[input_one] if mode_1 == 0 else input_one
            param_2 = puzzle_data[input_two] if mode_2 == 0 else input_two
            puzzle_data[input_three] = param_1 + param_2
            n += 4
        elif opcode == 2:
            input_two = puzzle_data[n + 2]
            input_three = puzzle_data[n + 3]
            param_1 = puzzle_data[input_one] if mode_1 == 0 else input_one
            param_2 = puzzle_data[input_two] if mode_2 == 0 else input_two
            puzzle_data[input_three] = param_1 * param_2
            n += 4
        elif opcode == 3:
            puzzle_data[input_one] = phase_setting if n == 0 else input_signal
            n += 2
        elif opcode == 4:
            if mode_1 == 0:
                output = puzzle_data[input_one]
            elif mode_1 == 1:
                output = puzzle_data[n + 1]
            n += 2
        elif opcode == 5:
            input_two = puzzle_data[n + 2]
            param_1 = puzzle_data[input_one] if mode_1 == 0 else input_one
            param_2 = puzzle_data[input_two] if mode_2 == 0 else input_two
            if param_1 != 0:
                n = param_2
            else:
                n += 3
        elif opcode == 6:
            input_two = puzzle_data[n + 2]
            param_1 = puzzle_data[input_one] if mode_1 == 0 else input_one
            param_2 = puzzle_data[input_two] if mode_2 == 0 else input_two
            if param_1 == 0:
                n = param_2
            else:
                n += 3
        elif opcode == 7:
            input_two = puzzle_data[n + 2]
            input_third = puzzle_data[n + 3]
            param_1 = puzzle_data[input_one] if mode_1 == 0 else input_one
            param_2 = puzzle_data[input_two] if mode_2 == 0 else input_two
            if param_1 < param_2:
                value = 1
            else:
                value = 0
            puzzle_data[input_third] = value
            n += 4
        elif opcode == 8:
            input_two = puzzle_data[n + 2]
            input_third = puzzle_data[n + 3]
            param_1 = puzzle_data[input_one] if mode_1 == 0 else input_one
            param_2 = puzzle_data[input_two] if mode_2 == 0 else input_two
            if param_1 == param_2:
                value = 1
            else:
                value = 0
            puzzle_data[input_third] = value
            n += 4
        else:
            return ("ERROR opcode: ", opcode)


def max_thruster(puzzle_data):
    current_max = 0
    perms = permutations("01234")
    for p in perms:
        output = intcode(puzzle_data, int(p[0]), 0)
        output = intcode(puzzle_data, int(p[1]), output)
        output = intcode(puzzle_data, int(p[2]), output)
        output = intcode(puzzle_data, int(p[3]), output)
        output = intcode(puzzle_data, int(p[4]), output)
        if output > current_max:
            current_max = output

    return current_max

for (test_in, test_out) in TEST_INPUTS:
    output = max_thruster(test_in)
    print("output: ", output)
    assert output == test_out

print(max_thruster(DAY_7_INPUT))
