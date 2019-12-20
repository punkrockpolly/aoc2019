from itertools import permutations


DAY_7_INPUT = [3,8,1001,8,10,8,105,1,0,0,21,46,55,68,89,110,191,272,353,434,99999,3,9,1002,9,3,9,1001,9,3,9,102,4,9,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,3,9,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,5,9,1002,9,2,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,102,3,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]  # noqa

TEST_INPUTS = [
    ([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], 139629729),  # noqa
    ([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10], 18216),  # noqa
]


def interpret_opcode(opcode):
    opcode = '0000' + str(opcode)
    instruction = int(opcode[-2:])
    mode_1 = int(opcode[-3:][0])
    mode_2 = int(opcode[-4:][0])

    return (instruction, mode_1, mode_2)


def intcode(puzzle_data, phase_setting, input_signal, n=0):
    length = len(puzzle_data)
    output = 0
    # print(n, puzzle_data)

    while n < length:
        (opcode, mode_1, mode_2) = interpret_opcode(puzzle_data[n])

        if opcode == 99:
            return n, puzzle_data, output, True

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
                return n + 2, puzzle_data, output, False
            elif mode_1 == 1:
                output = puzzle_data[n + 1]
                return n + 2, puzzle_data, output, False
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
            print("ERROR opcode: ", opcode)
            assert False


def max_thruster(puzzle_data):
    current_max = 0
    perms = permutations("56789")
    for p in perms:
        data = [puzzle_data.copy(), puzzle_data.copy(), puzzle_data.copy(), puzzle_data.copy(), puzzle_data.copy()]
        n = [0, 0, 0, 0, 0]
        outputs = [0, 0, 0, 0, 0]
        output = 0
        halt = False
        while not halt:
            for i, d in enumerate(data):
                n[i], d, output, halt = intcode(d, int(p[i]), output, n[i])
                if not halt:
                    outputs[i] = output
        if outputs[4] > current_max:
            current_max = outputs[4]

    return current_max

for (test_in, test_out) in TEST_INPUTS:
    output = max_thruster(test_in)
    print("output: ", output)
    assert output == test_out

print(max_thruster(DAY_7_INPUT))
