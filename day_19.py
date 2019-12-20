DAY_19_INPUT = [109,424,203,1,21101,0,11,0,1105,1,282,21101,18,0,0,1105,1,259,1202,1,1,221,203,1,21102,1,31,0,1106,0,282,21102,38,1,0,1106,0,259,21002,23,1,2,22102,1,1,3,21102,1,1,1,21102,1,57,0,1105,1,303,2102,1,1,222,20101,0,221,3,21001,221,0,2,21102,259,1,1,21102,1,80,0,1106,0,225,21102,62,1,2,21101,91,0,0,1105,1,303,2101,0,1,223,21001,222,0,4,21101,0,259,3,21101,0,225,2,21101,0,225,1,21101,0,118,0,1105,1,225,20102,1,222,3,21101,94,0,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1105,1,259,1202,1,1,223,20101,0,221,4,21001,222,0,3,21102,17,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,109,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21101,214,0,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22102,1,-3,1,22101,0,-2,2,21201,-1,0,3,21102,1,250,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21101,343,0,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22102,1,-4,1,21102,384,1,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2105,1,0]  # noqa


def interpret_opcode(opcode):
    opcode = '000' + str(opcode)
    instruction = int(opcode[-2:])
    mode_1 = int(opcode[-3:][0])
    mode_2 = int(opcode[-4:][0])
    mode_3 = int(opcode[-5:][0])

    return (instruction, mode_1, mode_2, mode_3)


def compute_mode(mode, input_param, state, relative_base):
    if mode == 0:
        return state[input_param]
    elif mode == 1:
        return input_param
    elif mode == 2:
        return state[input_param + relative_base]


def assign_value(mode, input_param, state, n, relative_base, value):
    if mode == 0:
        state[input_param] = value
    elif mode == 1:
        state[n] = value
    elif mode == 2:
        state[input_param + relative_base] = value


def intcode(puzzle_data, n=0, relative_base=0):
    puzzle_data.extend([0 for _ in range(5000)])

    while True:
        (opcode, mode_1, mode_2, mode_3) = interpret_opcode(puzzle_data[n])

        if opcode == 99:
            print('HALT opcode: 99')
            break

        input_one = puzzle_data[n + 1]

        if opcode == 1:
            input_two = puzzle_data[n + 2]
            input_three = puzzle_data[n + 3]
            param_1 = compute_mode(mode_1, input_one, puzzle_data, relative_base)
            param_2 = compute_mode(mode_2, input_two, puzzle_data, relative_base)
            value = param_1 + param_2
            assign_value(mode_3, input_three, puzzle_data, n + 3, relative_base, value)
            n += 4
        elif opcode == 2:
            input_two = puzzle_data[n + 2]
            input_three = puzzle_data[n + 3]
            param_1 = compute_mode(mode_1, input_one, puzzle_data, relative_base)
            param_2 = compute_mode(mode_2, input_two, puzzle_data, relative_base)
            value = param_1 * param_2
            assign_value(mode_3, input_three, puzzle_data, n + 3, relative_base, value)
            n += 4
        elif opcode == 3:
            instance_input = yield  # INPUT
            assign_value(mode_1, input_one, puzzle_data, n + 1, relative_base, instance_input)
            n += 2
        elif opcode == 4:
            if mode_1 == 0:
                output = puzzle_data[input_one]
            elif mode_1 == 1:
                output = input_one
            elif mode_1 == 2:
                output = puzzle_data[input_one + relative_base]
            n += 2
            instance_input = yield output  # OUTPUT
        elif opcode == 5:
            input_two = puzzle_data[n + 2]
            param_1 = compute_mode(mode_1, input_one, puzzle_data, relative_base)
            param_2 = compute_mode(mode_2, input_two, puzzle_data, relative_base)
            if param_1 != 0:
                n = param_2
            else:
                n += 3
        elif opcode == 6:
            input_two = puzzle_data[n + 2]
            param_1 = compute_mode(mode_1, input_one, puzzle_data, relative_base)
            param_2 = compute_mode(mode_2, input_two, puzzle_data, relative_base)
            if param_1 == 0:
                n = param_2
            else:
                n += 3
        elif opcode == 7:
            input_two = puzzle_data[n + 2]
            input_three = puzzle_data[n + 3]
            param_1 = compute_mode(mode_1, input_one, puzzle_data, relative_base)
            param_2 = compute_mode(mode_2, input_two, puzzle_data, relative_base)
            if param_1 < param_2:
                value = 1
            else:
                value = 0
            assign_value(mode_3, input_three, puzzle_data, n + 3, relative_base, value)
            n += 4
        elif opcode == 8:
            input_two = puzzle_data[n + 2]
            input_three = puzzle_data[n + 3]
            param_1 = compute_mode(mode_1, input_one, puzzle_data, relative_base)
            param_2 = compute_mode(mode_2, input_two, puzzle_data, relative_base)
            if param_1 == param_2:
                value = 1
            else:
                value = 0
            assign_value(mode_3, input_three, puzzle_data, n + 3, relative_base, value)
            n += 4
        elif opcode == 9:
            if mode_1 == 0:
                relative_base += puzzle_data[input_one]
            elif mode_1 == 1:
                relative_base += input_one
            elif mode_1 == 2:
                relative_base += puzzle_data[input_one + relative_base]
            n += 2
        else:
            print("ERROR opcode: ", opcode)
            assert False


def tractor_beam(puzzle_data):
    width = 50
    height = 50
    grid = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            computer = intcode(puzzle_data.copy())
            computer.send(None)
            computer.send(x)
            grid[y][x] = computer.send(y)

    return sum(map(sum, grid))

print(tractor_beam(DAY_19_INPUT))
