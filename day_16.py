from copy import copy
import numpy


DAY_16_INPUT = "59702216318401831752516109671812909117759516365269440231257788008453756734827826476239905226493589006960132456488870290862893703535753691507244120156137802864317330938106688973624124594371608170692569855778498105517439068022388323566624069202753437742801981883473729701426171077277920013824894757938493999640593305172570727136129712787668811072014245905885251704882055908305407719142264325661477825898619802777868961439647723408833957843810111456367464611239017733042717293598871566304020426484700071315257217011872240492395451028872856605576492864646118292500813545747868096046577484535223887886476125746077660705155595199557168004672030769602168262"  # noqa

TEST_INPUTS = [('12345678', 4, [0, 1, 0, 2, 9, 4, 9, 8]),
               ('80871224585914546619083218645595', 100, [2, 4, 1, 7, 6, 1, 7, 6]),
               ('19617804207202209144916044189917', 100, [7, 3, 7, 4, 5, 4, 1, 8]),
               ('69317163492948606335995924319873', 100, [5, 2, 4, 3, 2, 1, 3, 3]),
               ]


def fft(puzzle_input, phases):
    base_pattern = [0, 1, 0, -1]
    input_array = numpy.array([int(elem) for elem in puzzle_input])
    puzzle_array = copy(input_array)

    for _ in range(phases):  # loop through phases
        pattern = []
        for i in range(len(puzzle_array)):  # loop through each input character
            repeating_pattern = []
            for ipattern in range(4):  # repeat base pattern
                repeating_pattern += [base_pattern[ipattern]] * (i + 1)
            if len(repeating_pattern) < len(puzzle_array) + 1:  # scale size of repeating pattern
                scale = len(puzzle_array) // len(repeating_pattern) + 1
                repeating_pattern = repeating_pattern * scale
            repeating_pattern = repeating_pattern[1:len(puzzle_array) + 1]  # skip first value
            pattern.append(numpy.abs(numpy.sum(
                numpy.array(repeating_pattern) * puzzle_array)) % 10)  # numpy to sum, multiply, keep first digit

        puzzle_array = numpy.array([int(elem) for elem in pattern])  # output list used in next phase

    return puzzle_array[0:8]


for (test_in, phases, test_out) in TEST_INPUTS:
    print(test_in)
    output = fft(test_in, phases)
    print("output: ", output)
    assert numpy.array_equal(output, test_out)

print(fft(DAY_16_INPUT, 100))
