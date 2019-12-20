DAY_20_INPUT = """                                         J       F           Z     S   X           H     T
                                         Q       V           V     K   P           K     D
  #######################################.#######.###########.#####.###.###########.#####.###########################################
  #...#...#.#...........#.#.....#.#.....#...#.#.#.....#.#...#...#...#.#...#.........#.#...................#.#.#.#...#.#.....#.......#
  ###.###.#.#######.#####.#.#.#.#.###.#.###.#.#.#.###.#.###.#.#####.#.#.#.#######.###.#.#.#.###.###.#.###.#.#.#.###.#.###.#.###.###.#
  #.#.....#.#.#.#.#...#.#...#.#.....#.#.....#.......#.#.........#...#...#.#.....#.....#.#.#.#.#...#.#.#.#.......#...#.....#.#.....#.#
  #.#####.#.#.#.#.#.###.#########.#.###.#.#####.#######.#.#########.###.#####.#.#####.#.#####.#########.#.#######.#.###.#####.#.#.#.#
  #.#...#.....#...#...#.....#...#.#.....#.#.#.......#...#.#...#.....#.#.......#.#.....#.#...........#...#.#.#.....#.#.......#.#.#.#.#
  #.###.#.###.###.###.###.###.#####.###.###.###.#########.#.#.#.#.###.#######.#####.###.#.#.###########.###.#.#######.###.###.#####.#
  #...#.#.#.#...#.#.....#...#.........#.....#.#...#.........#.#.#.....#.........#.#.#.#...#...#...#.......#.....#...#.#.#.#.#.#.#.#.#
  ###.#.###.###.#.###.###.###############.###.#.###.#.###.###.#######.#.###.#####.#.#.#.#.###.#.#######.###.#####.###.#.###.#.#.#.###
  #.#.................#.#.#...#...#.........#...#.#.#.#...#.....#.#...#.#.....#.#.....#.#.#.......#.#.......#.....#.#.#.............#
  #.#################.#.#.###.#.#####.#.###.###.#.###.#.#.###.###.#.###.#######.#.###.#####.#######.###.###.###.###.#.#.###.###.#####
  #.#...#...#...#.#...............#.#.#.#...#.......#.#.#...#.#.......#.......#...#...#...#...............#.......#.......#.#.....#.#
  #.###.#.#####.#.#.#####.#####.###.#####.#####.#.###########.###.#.#.#.#######.###.#.#.#.###.#####.###.#########.###.#.###########.#
  #...#.....#.#.....#...#.#.#.#.............#...#.#.#...#.#...#...#.#.#.#...#...#...#.#.#.........#...#.....#...#.#...#...#.#.#.#...#
  #.###.###.#.#####.###.#.#.#.###.#######.#.###.###.###.#.###.###.###.#.#.#########.#.###.#.###.###.#####.###.#######.#####.#.#.###.#
  #...#...#.#.#...#.#.....#.............#.#...#.......#...#.....#.#...#.....#...#.#.#.#...#.#.....#.....#.....#.....#.#.#...#.#.....#
  ###.#.#####.###.###.#.#.###.#.#.#######.###.###.###.#.#.###.#.#####.###.###.###.#.#.#.#######.###.#.###########.###.#.###.#.###.###
  #.#...#.#...........#.#.#...#.#.#...#...#...#.#...#.#.#.....#.#.#...#...........#.#.#...#.#.....#.#.....#.#...#.#.....#.#...#.#...#
  #.#.###.#.#####.#.#.###.#########.#####.###.#.#.###########.###.###.#.#.#.###.#####.#.###.###########.###.###.#.###.###.#.###.#.###
  #.#.....#.#.....#.#.#.......#.....#...#.#...#.....#.....#.#.....#...#.#.#...#.....#.#.#.#...#...#.#.....#.#.......#.........#.#.#.#
  #.#.###########################.#####.###.#.#.#########.#.#.#######.#.#######.#.###.#.#.#.###.#.#.#.#.###.###.#####.#.###.###.#.#.#
  #.....#.....#.#...#.....#.#...#.....#.#.#.#.#...#...#.#...#...#.....#.....#.#.#.#...#...#.....#...#.#.#.....#.#.#.#.#...#.#.#.....#
  #.#.###.#####.#.#.#####.#.###.###.###.#.###.#.###.###.#.#.#.#######.#.#.###.#.#####.###.#.###############.###.#.#.###.#####.###.###
  #.#.....#...#...#.....#.#.....#...#.#...#...#.......#...#...#.......#.#.#.#...#...#.#.....#.#.#.....#.#.................#...#.#...#
  ###.#######.#####.#.#.#.#####.#.#.#.###.###.#.#.###.#.#######.###.###.###.###.#.#.#.#.#.###.#.###.###.#######.###.#####.###.#.#.###
  #...#.#.#...#.#.#.#.#.....#.#.#.#...#.....#.#.#...#.#.....#.#.#...#.....#...#.#.#...#.#.#.#.......#.....#.#.....#.....#.#.....#.#.#
  #.#.#.#.#.###.#.#########.#.#.#####.###.###.#.#.###.#.#.#.#.#####.###.#.###.#####.###.###.#.###.#.###.#.#.###.#############.###.#.#
  #.#.#.#...#.#.#.....#.............#.#.....#.#.#.#...#.#.#.....#.....#.#.....#...#...#...#.#.#.#.#...#.#.#...#.#...#.#...#.....#...#
  #.###.#.###.#.###.#####.###.#####.#.#####.#.###.###.#######.#######.###.###.###.###.#.###.#.#.###.#####.###.#.###.#.###.###.###.#.#
  #...#.....#...#.#.....#.#.#...#.#.............#.#.....#...#.....#.#...#.#...#...#...#.......#...#.#.#...#.....#.#...#.....#...#.#.#
  #.#######.###.#.###.#####.#####.#####.#.###.###.###.#####.#.#####.#.#######.#.#.#.#####.###.#.#####.###.#.#####.###.###.#####.###.#
  #...#.#.....#.....#...#...#...#.#.....#.#...#.#.#...#.......#...#.#...#.....#.#.#...#...#...#...#...#.#.....#.#.#.#.#...#...#...#.#
  #.###.###.###.#######.#.#####.#.###########.#.#.###.#.###.###.#.#.#.#######.#.#.###.###.#.###.###.###.#.###.#.#.#.#.###.#.###.###.#
  #.#.#.............#.#...#.#.#...#.#...........#.#...#...#...#.#.........#...#.#.......#.#.......#.........#.....#.#...#...........#
  #.#.#.#####.#.#.#.#.#.#.#.#.#.###.#####.#########.#####.#####.###########.###.#############.#######.#.###########.###.#######.#.###
  #...#.#...#.#.#.#.#...#.#.#...#...#    J         R     L     Y           L   I             X    #.#.#.#.#.#.#...#.#...#.....#.#.#.#
  #.###.#.###########.#####.###.#.###    N         P     P     L           S   B             P    #.###.#.#.#.#.###.#.#######.#.###.#
  #...#.#...........#.#.#.#...#...#.#                                                             #.#.....#.........#.....#.#...#.#..AA
  #.###.#.#.#########.#.#.###.#.###.#                                                             #.###.#.#.#.###.#.#.###.#.###.#.#.#
YL..#.....#.#.#.#.#.#.#..............EK                                                           #.....#.#.#.#...#...#.......#.#....UT
  #.###.#.###.#.#.#.#.###.#####.###.#                                                             #.#####.#.#.#.###.###.#######.###.#
  #.....#.......#.......#.#.#.#.#.#.#                                                           ZV..#...#.#.#.#...#...#.#.....#.....#
  #####.###.###.#######.###.#.#.#.###                                                             #.#.###.#.###.#######.###.#.#.#.#.#
  #.......#...#.#.........#.........#                                                             #.#.#.#.....#.#...#.......#...#.#.#
  #########.#######.###.#.#.###.#####                                                             ###.#.#.#.#.#.#.#########.###.###.#
  #.#...#...........#...#...#.#.#...#                                                             #.....#.#.#.#.#.........#...#.#.#.#
  #.###.#####################.#####.#                                                             ###.#.#########.#.#.###.#######.###
  #.............#...........#...#.#..YS                                                           #...#.#...#.#.#.#.#.#.........#...#
  #####.###.###.#.#####.###.###.#.#.#                                                             #.#.#.#.###.#.#####.#####.#######.#
  #.......#...#.......#...#.........#                                                           FV..#.#...#.....#...#...#...#...#...#
  ###.#.#.#.#.#.#.###.#.###.###.###.#                                                             #####.#####.#.###.###.#.###.#.#.#.#
JB..#.#.#.#.#.#.#...#.#.#.....#.#.#.#                                                             #...........#.........#.....#...#..ZP
  #.#.###########.#.###.#########.###                                                             #.#.#######################.#######
ZZ....#.....#.#.#.#.#.....#.........#                                                             #.#.#.#...#.#.............#.#......IB
  #.#####.###.#.#######.###.###.#####                                                             #####.#.#.#.#.#.#.#.#####.###.#.#.#
  #.#...........#.....#.#...#.#.....#                                                           QR......#.#.#...#.#.#...#.....#.#.#.#
  ###.#.#####.#####.#########.#.###.#                                                             #####.#.#.#.#####.#########.#.###.#
  #.#.#...#.#.....#.#.......#.....#.#                                                             #.#.....#.....#...#.#...#...#...#.#
  #.#####.#.###.###.###.#####.#.#.#.#                                                             #.###.#.###.###.#.#.#.###.###.#####
  #.#...#.....#...#.#.#.#.#.#.#.#.#..ZP                                                           #...#.#...#...#.#.#.#.#.......#.#.#
  #.#.#.#####.#.###.#.#.#.#.#####.###                                                             #.#################.#.#.#.#####.#.#
YS....#.......#...................#.#                                                           TD..#...#.....#.#...#.#.#.#.#.....#..ZJ
  #######.###.#########.###.#.###.#.#                                                             #.###.###.###.#.###.#.###.#.###.#.#
EK......#.#.#...#.........#.#.#.....#                                                             #.......#...#.....#.#.#...#...#.#.#
  #####.###.#####.#.#################                                                             ###.#.###.###.#.###.#.#######.#.#.#
  #.....#.#.#...#.#.#.#.#.....#.#...#                                                             #...#.#.....#.#.#.....#.......#...#
  ###.#.#.#.#.#######.#.#.###.#.#.###                                                             #####.###.###.#.###.#.###.#.#.#.#.#
  #...#.#.......#.........#.#.#.#...#                                                             #.#.#.........#.....#.....#.#.#.#.#
  ###.###.###.#.#####.###.#.#.#.#.###                                                             #.#.#######################.#######
  #.#.......#.#.......#.#.#.#........QP                                                           #...#...#...........#.....#.#.....#
  #.###########.#####.#.###.#########                                                             #.#.#.#.#.###.#####.#.#.#####.###.#
MP........#...#...#...#.......#.....#                                                             #.#...#.....#.#.....#.#.....#...#.#
  #######.#.#########.#.#####.#.###.#                                                             #.###.#.#.#.#.#####.#.#####.###.#.#
  #.........#...#...#.#.#.....#...#..TV                                                         NU....#.#.#.#.#.#.........#.....#.#..RP
  #.###.#######.#.#####.###.#####.###                                                             #.###.###############.#######.#.###
  #.#...#.......#.#.#...#...#.....#.#                                                             #.#.#...#...#.#...#.#.#...#.......#
  #.#####.#.#####.#.#.#####.###.###.#                                                             ###.#.###.###.###.#.###.#####.#####
  #.......#...........#...#.....#.#.#                                                           RX....#.#.#.#.....#.#.#...#.#...#....JN
  #######.#######.#.#.#.#########.#.#                                                             #.#####.#.#.#####.#.#.#.#.#######.#
  #...#.......#...#.#.#.....#...#....MP                                                           #.#.#...#...#.........#.#.....#...#
  #.###################.###.#.#.#.#.#                                                             #.#.###.###.#####.#.#.#####.#####.#
OF..#...#...#...#.#.#.....#...#.#.#..NZ                                                           #.#.....#...#...#.#.#.#.#.#.#.#.#.#
  #.###.###.###.#.#.###.#.#####.#.#.#                                                             #.#.#.###.#.###.###.#.#.#.#.#.#.#.#
QP..#...#...........#...#.#.....#.#.#                                                             #...#.....#.........#.............#
  #.#.#.###.###.#.#.#####.#.#####.###                                                             #.#.#.#.###.###.###.#.#.#.#.###.#.#
  #...#.....#...#.#.......#.......#.#                                                             #.#.#.#...#.#.#.#...#.#.#.#.#.#.#.#
  #.#####.###.#.#.#.#.#.###.#.#.#.#.#      O           U     J   J       Z         H       S      ###.#####.#.#.#####.#.#.#####.#.###
  #.....#.#...#.#.#.#.#.#...#.#.#...#      F           T     Q   B       J         K       K      #.....#.#.#.#.......#.#...#.......#
  #.#.###.#.#.#.###.#.#.###.###.#.#########.###########.#####.###.#######.#########.#######.###########.#.#####.#.#.#.#####.###.#####
  #.#...#.#.#.#...#.#.#.#.....#.#...#.......#...#.#...#.#.....#.........#...#...#.....#.#...#...#...........#...#.#.#.....#.#.......#
  #.#.###.#.#.#.###.#.###.#####.#.#######.###.#.#.#.#.#.###.#######.#######.#.#.#.#####.###.#.###.#####.#.###.#.#####.#########.#.#.#
  #.#.#.#.#.#.#...#.#...#...#...#...#...#.....#...#.#...#.#...#.#...#...#...#.#.#...#.#.#.......#...#...#...#.#.#.......#.#.....#.#.#
  #.#.#.###.###.#.#######.#.###.#######.#######.#.#.#####.#.#.#.#.#####.#.###.#.#.###.#.#.#####.#########.###.###.#.###.#.#.###.#.###
  #.#.#.#...#...#.#.......#...#.#...#.#.....#...#.#...#.....#...#.#...........#.#.......#...#.#.....#.....#.....#.#.#.....#...#.#.#.#
  #.#.#.#.#.###.###.###.###.#######.#.#.#.#.#.#.#####.#####.#####.###.###.#.###.###.###.###.#.#######.#.#.#######.#.#####.#####.###.#
  #.#...#.#.#...#.....#.#...#...........#.#...#.#.#.....#.....#.#...#.#...#.#.#...#...#.#.......#...#.#.#...#.....#...#...#.#.......#
  #.#.###.#.#######.#.#####.#.###.###.###.#######.#.#.###.#####.#.#####.#.###.#.#######.#.###.#.#.#####.#.#####.###.#.###.#.###.###.#
  #.#...#.#.....#.#.#.#...#.#.#.#...#.#...#.......#.#...#.......#.....#.#...#...#...#.#.#...#.#.#.....#.#.#.#.....#.#.#.....#.#...#.#
  #.#.#####.#.###.#.#.###.#.###.#.#######.#.#.###.#####.###.###.###.#########.#.#.###.#.#.#####.#.#####.###.#.###.###.###.#.#.#.###.#
  #.#.#.....#...#.#.#.#.....#.....#.........#.#.....#.#...#.#...#.......#.#...#...#.....#...#.........#.#.....#.#...#.#...#...#...#.#
  ###.###.###.###.#######.#.#####.###########.#####.#.#.#######.#.#.###.#.#####.#####.###.###.###.###########.#.###.#####.#####.#.#.#
  #.#.#.#...#...#.....#...#...#...#...............#.#...#.......#.#...#...#.#.....#.#...#...#.#.#.#.#.#.#.#.......#...#.....#...#.#.#
  #.#.#.#.###.###.#.###.###.#######.#.#.#.#.###########.#####.#.#.#.#####.#.#.#.###.###.#.#####.###.#.#.#.#####.#########.#.#####.###
  #.....#.#.#...#.#.....#.......#.#.#.#.#.#.#.......#...#.....#.#.#.#.#...#.#.#.#...#...#.....#.#.#.#.#.....#.....#.......#.#...#...#
  #.#.###.#.#.#######.#.#.###.###.#######.#######.###.#######.###.###.#####.#.#.#.#.###.#.#####.#.#.#.#.###########.#.#.#.###.###.###
  #.#...#...#.#.....#.#.#.#...#.#.#.#...........#.#.....#.....#...#...#.....#.#...#.#...#...#.#...#.....#.#.....#.#.#.#.#.......#.#.#
  #.#####.#.#####.#####.#.#.###.#.#.#####.#.#####.#.###.###.#.###.###.###.#.###.#######.#.###.#.###.###.#.###.###.#.#.###.#####.#.#.#
  #...#...#...#.........#.#.#.........#...#.#.....#.#.....#.#.#.#.....#.#.#.......#.#...#.......#.#.#.#.#.....#...#.#.#.......#.#...#
  #.###.#.#.#.###.###.###.#######.###.###.#.#####.###.#.#####.#.#.#.###.###.###.###.###.###.#.###.#.#.###.#####.###.#####.#######.#.#
  #...#.#.#.#.#.#...#...#...#.#.....#...#.#.....#.....#...#.....#.#.#.#.....#.#.#.#.....#...#...............#.....#.....#...#.#...#.#
  #.###.#.#.###.#.###.#######.#.#.#####.#.#######.#.###.###.###.#.###.###.#.#.###.###.#####.#.#.###.#########.#####.#.#####.#.#######
  #.#.#.#.#.#.....#...#.#.#.....#.#.......#.#.#.#.#...#.#.#.#.#.#.#.....#.#.....#...#.....#.#.#...#...#...#...#...#.#...#.....#.....#
  ###.#.###.#.#.###.###.#.#.#.#.###.#####.#.#.#.#.#######.###.#.#.#.#.#.#######.###.###.#######.#########.###.#.#.#.#######.###.#.###
  #.#...#.#.#.#...#.#.......#.#.#...#...........#.#...#.........#.#.#.#...#.....#.........#.#.#...#.....#.....#.#.#.#.#.#.#.....#...#
  #.###.#.#.###.#.#.#.#.###.###.#.#######.#.###.#.#.#####.#####.#.###.#.###.#.#.#.###.#####.#.#.#######.#.###.###.###.#.#.###.#.#.#.#
  #.....#...#...#.#.#.#.#...#...#.#...#...#.#.#.#.......#.#.....#.#...#...#.#.#.#...#.#.#.#.......#.#.......#.#.#.......#.#...#.#.#.#
  #.#.#########.###.#.#####.###.#####.###.###.#.#######.#####.###.#.###.#####.###.###.#.#.#.#.#.###.#####.###.#.#.#######.#####.###.#
  #.#.#...........#.#.#.....#.#.#.....#.#.#.....#.#.#.....#...#...#.#.#.#.#.#.#...#.#.#.#...#.#.....#.#.....#.#.#.............#.#...#
  #######.###.#.###.#.#.#####.###.###.#.#.###.###.#.#.#######.###.#.#.#.#.#.#.###.#.###.#.###.#######.###.#####.#.###################
  #...#...#...#...#.#.#...#.#...#.#.....#.#.#.....#.....#.......#...#.......#...#.......#.#.#...........#.#.#.#.#.#...........#.#.#.#
  ###.#.#####.#####.#.###.#.###.#.###.#.###.###.#.#.###.###.#.#.#.#.#.#########.#######.###.#.#.#########.#.#.#.#.#.#####.#.###.#.#.#
  #.........#.#.....#.#...#.......#...#.........#.#.#.....#.#.#.#.#.#...#.......#...........#.#.........................#.#.........#
  #########################################.#######.###########.#######.###.#####.#############.#####################################
                                           L       R           N       L   T     N             Q
                                           P       X           Z       S   V     U             R
"""  # noqa


def parse_input(puzzle_input):
    donut_map = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            if char == ' ':
                continue
            elif char == '#':
                donut_map[(x, y)] = 'WALL'
            elif char == '.':
                donut_map[(x, y)] = 'PATH'
            else:
                donut_map[(x, y)] = 'PORTAL'

    return donut_map


def traverse_maze(puzzle_input):
    pass


print(parse_input(puzzle_input=DAY_20_INPUT))
