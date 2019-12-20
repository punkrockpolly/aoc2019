from copy import deepcopy
from collections import defaultdict


DAY_11_INPUT = [3,8,1005,8,344,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,28,1006,0,40,2,1009,2,10,1,1108,13,10,1,1007,6,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,66,1006,0,91,2,103,5,10,1006,0,12,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,98,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,120,1,1001,15,10,2,102,4,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,149,1,106,9,10,1,5,5,10,1,1106,6,10,2,5,15,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,187,2,1106,9,10,2,9,13,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,218,1,1106,3,10,1006,0,13,2,1005,15,10,2,1006,19,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,254,2,1108,14,10,1006,0,33,1,7,20,10,2,105,6,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,292,1006,0,82,2,6,7,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,320,1006,0,11,101,1,9,9,1007,9,979,10,1005,10,15,99,109,666,104,0,104,1,21102,932700857100,1,1,21101,0,361,0,1106,0,465,21102,825599210392,1,1,21102,1,372,0,1106,0,465,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,29195529219,0,1,21101,419,0,0,1106,0,465,21101,0,235324673063,1,21102,1,430,0,1105,1,465,3,10,104,0,104,0,3,10,104,0,104,0,21102,988225098508,1,1,21102,453,1,0,1106,0,465,21102,988753318756,1,1,21101,464,0,0,1106,0,465,99,109,2,22101,0,-1,1,21102,40,1,2,21101,0,496,3,21101,0,486,0,1105,1,529,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,491,492,507,4,0,1001,491,1,491,108,4,491,10,1006,10,523,1101,0,0,491,109,-2,2106,0,0,0,109,4,2102,1,-1,528,1207,-3,0,10,1006,10,546,21102,0,1,-3,21201,-3,0,1,22102,1,-2,2,21101,0,1,3,21102,565,1,0,1105,1,570,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,593,2207,-4,-2,10,1006,10,593,22102,1,-4,-4,1105,1,661,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,612,0,0,1106,0,570,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,631,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,653,21202,-1,1,1,21101,0,653,0,106,0,528,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]  # noqa

TEST_INPUTS = [
    (),  # noqa
]


def interpret_opcode(opcode):
    opcode = '00000' + str(opcode)
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


def intcode(puzzle_data, instance_input, n=0, relative_base=0):
    puzzle_data.extend([0 for _ in range(5000)])
    output = []

    while True:
        (opcode, mode_1, mode_2, mode_3) = interpret_opcode(puzzle_data[n])

        if opcode == 99:
            return ((0, 0), True, n, relative_base)

        if len(output) == 2:
            return (output, False, n, relative_base)

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
            assign_value(mode_1, input_one, puzzle_data, n + 1, relative_base, instance_input)
            n += 2
        elif opcode == 4:
            if mode_1 == 0:
                output.append(puzzle_data[input_one])
            elif mode_1 == 1:
                output.append(input_one)
            elif mode_1 == 2:
                output.append(puzzle_data[input_one + relative_base])
            n += 2
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


grid = defaultdict(int)
grid_copy = deepcopy(grid)


def hull_robot(grid, grid_copy, puzzle_data):
    position = (100, 100)
    current_direction = 0
    halt = False
    n = 0
    relative_base = 0

    while not halt:
        output, halt, n, relative_base = intcode(puzzle_data, grid[position], n, relative_base)
        color, direction = output
        grid[position] = color
        grid_copy[position] = 1

        if not halt:
            if direction == 1:
                current_direction += 1
            else:
                current_direction -= 1
            current_direction %= 4

            y, x = position
            if current_direction == 0:
                x -= 1
            elif current_direction == 1:
                y += 1
            elif current_direction == 2:
                x += 1
            elif current_direction == 3:
                y -= 1

            position = (y, x)

    return grid_copy


painted_output = hull_robot(grid, grid_copy, DAY_11_INPUT)
total = len(painted_output)
print(total)
