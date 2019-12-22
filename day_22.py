DAY_22_INPUT = """cut 1470
deal with increment 46
cut -6481
deal with increment 70
cut 547
deal with increment 48
cut -6479
deal with increment 69
cut -5203
deal with increment 13
deal into new stack
deal with increment 73
deal into new stack
cut -6689
deal with increment 61
cut -9853
deal with increment 48
cut -9673
deal into new stack
deal with increment 3
deal into new stack
deal with increment 64
cut 5789
deal with increment 66
deal into new stack
deal with increment 70
cut -2588
deal with increment 6
deal into new stack
deal with increment 6
cut -7829
deal with increment 49
deal into new stack
deal with increment 19
cut 9777
deal into new stack
deal with increment 27
cut 6210
deal into new stack
deal with increment 12
cut 6309
deal with increment 12
cut -9458
deal with increment 5
cut 6369
deal with increment 27
cut 2278
deal with increment 42
cut 6656
deal with increment 62
cut -1424
deal with increment 25
deal into new stack
deal with increment 12
deal into new stack
cut -7399
deal into new stack
cut -8925
deal with increment 47
deal into new stack
cut 5249
deal with increment 65
cut -213
deal into new stack
cut 6426
deal with increment 22
cut -6683
deal with increment 38
deal into new stack
deal with increment 62
cut 6855
deal with increment 75
cut 4965
deal into new stack
cut -5792
deal with increment 30
cut 9250
deal with increment 19
cut -948
deal with increment 26
cut -5123
deal with increment 68
cut -604
deal with increment 41
deal into new stack
deal with increment 45
cut 5572
deal into new stack
cut 3853
deal with increment 21
cut 1036
deal into new stack
deal with increment 6
cut 8114
deal into new stack
deal with increment 38
cut -5
deal with increment 58
cut 9539
deal with increment 19"""


TEST_INPUTS = [
    ("""deal with increment 7
deal into new stack
deal into new stack""", [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]),
    ("""cut 6
deal with increment 7
deal into new stack""", [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]),
    ("""deal with increment 7
deal with increment 9
cut -2""", [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]),
    ("""deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1""", [9, 2, 5, 8, 1, 4, 7, 0, 3, 6])
]


def slam_shuffle(puzzle_data, num_cards=10007):
    deck = [i for i in range(num_cards)]

    for line in puzzle_data.splitlines():
        if line.startswith('deal with increment '):
            n = int(line[20:])
            deck = deal_with_increment_n(deck, n)
        elif line.startswith('cut '):
            n = int(line[4:])
            deck = cut_n_cards(deck, n)
        elif line == 'deal into new stack':
            deck = deal_into_new_stack(deck)

    return deck


def cut_n_cards(deck, n):
    return deck[n:] + deck[:n]


def deal_with_increment_n(deck, n):
    size = len(deck)
    deck2 = [0] * size
    for i, elem in enumerate(deck):
        j = i * n % size
        deck2[j] = elem
    return deck2


def deal_into_new_stack(deck):
    deck.reverse()
    return deck


for (test_in, test_out) in TEST_INPUTS:
    print(test_in)
    output = slam_shuffle(test_in, 10)
    print("output: ", output)
    print("expected output: ", test_out)
    assert output == test_out

print(slam_shuffle(DAY_22_INPUT).index(2019))
