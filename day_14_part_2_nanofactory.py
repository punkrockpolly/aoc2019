from collections import defaultdict
from math import ceil


DAY_14_INPUT = """2 MPHSH, 3 NQNX => 3 FWHL
144 ORE => 1 CXRVG
1 PGNF => 8 KHFD
3 JDVXN => 5 FSTFV
1 ZMZL, 30 PVDSG => 6 SMBH
1 CFDNS, 2 PTZNC, 10 XCKN => 9 SKVP
1 JWNR => 1 QCVHS
10 MHRML => 1 KXNWH
4 PVDSG => 3 VBZJZ
10 TLBV => 1 ZVNH
1 PVQB, 5 JDVXN => 4 WDPCN
4 NQNX, 7 KHFD, 9 SDWSL => 6 HWVM
1 SMBH => 2 PCWR
1 CXNZD, 5 SKVP, 7 LVWTF => 9 QFQJV
2 HWVM => 7 GPXP
3 CXRVG, 3 GXNL => 8 PVDSG
1 PTZNC, 2 CFDNS => 7 LCKSX
14 NQNX, 8 FWHL => 5 XCKN
12 PVDSG, 3 PVQB => 8 TLBV
8 PVQB => 8 ZKCK
1 GPXP => 5 LCGN
5 VGNR, 1 ZMZL => 9 SMGNP
2 SMGNP => 7 CXNZD
6 SMGNP, 2 HWVM, 9 PTZNC => 7 GLMVK
18 QNZVM => 7 NLCVJ
1 JDVXN, 10 GMFW, 6 VBZJZ => 9 ZMZL
1 HCFRV, 1 ZKCK, 1 SMGNP, 1 LCKSX => 7 JXZFV
13 NLCVJ, 6 ZMZL => 7 SDWSL
3 SMBH => 4 PVQB
20 QNZVM, 1 PTZNC, 7 PVQB => 7 HFLGH
2 CXNZD => 8 VLNVF
4 GMFW => 4 JDVXN
23 VGNR => 3 HSBH
1 FWHL, 32 MPHSH => 7 ZNSV
5 WDPCN, 6 ZKCK, 3 QNZVM => 4 MWHMH
1 FSTFV, 3 ZKCK, 1 LVWTF => 9 LGHD
2 SKVP, 2 MWHMH, 12 QCVHS, 6 HFLGH, 3 NRGBW, 1 ZVNH, 2 LGHD => 4 SBQKM
13 PVQB, 2 HSBH, 5 TLBV => 9 LVWTF
6 FSTFV => 2 JWNR
7 ZKCK => 9 NRGBW
8 HFLGH, 3 KXNWH, 15 VLNVF, 2 VGNR, 2 SDMS, 10 MWHMH, 7 KHFD, 1 FSTFV => 4 WTRPM
5 SKVP => 4 SDMS
100 ORE => 7 GMFW
9 GXNL => 7 MPHSH
2 GXNL, 5 GMFW => 9 NQNX
3 SDWSL, 8 LVWTF, 2 GPXP => 5 HCFRV
140 ORE => 4 GXNL
1 WDPCN, 4 NLCVJ => 1 MHRML
1 VBZJZ => 7 PGNF
1 ZNSV => 1 CFDNS
1 GLMVK, 7 SDMS => 5 GBZRN
14 WTRPM, 93 SBQKM, 37 JXZFV, 4 NRGBW, 12 QFQJV, 24 SMBH, 3 LCGN, 15 GBZRN, 16 PCWR, 11 XCKN => 1 FUEL
1 WDPCN, 5 FWHL => 8 PTZNC
1 ZNSV => 9 VGNR
5 PGNF => 5 QNZVM
"""


TEST_INPUTS = [
    ("""157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
""", 82892753),
    ("""2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF
""", 5586022)
]


def parse_reactions(puzzle_input):
    """
    input: 5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
    output: {'GNMV': {quantity: 6, ingredients: {'VJHF': 5, 'MNCFX': 7, 'VPVL': 9, 'CXFTF': 37}}}
    """
    reactions = defaultdict(dict)
    for line in puzzle_input.splitlines():
        input_chemicals, output_chemical = line.split(' => ')
        num_output, output_chem = output_chemical.split()
        reactions[output_chem]['quantity'] = int(num_output)

        input_chems = [chem for chem in input_chemicals.split(', ')]
        reactions[output_chem]['ingredients'] = {
            chem: int(value) for value, chem in [input_chem.split() for input_chem in input_chems]}

    return reactions


def ensure(reactions, data, chem, quantity):
    if data[chem] >= quantity:
        return True
    if chem == 'ORE':
        return False

    n = ceil((quantity - data[chem]) / reactions[chem]['quantity'])
    ensured = True
    for sub_chem, sub_quantity in reactions[chem]['ingredients'].items():
        ensured = ensured and ensure(reactions, data, sub_chem, n * sub_quantity)
        data[sub_chem] -= n * sub_quantity
    if ensured:
        data[chem] += n * reactions[chem]['quantity']

    return ensured


def nanofactory(puzzle_input):
    reactions = parse_reactions(puzzle_input)
    low, high = 0, 10**12
    while low < high - 1:
        mid = low + (high - low) // 2
        data = {element: 0 for element in reactions}
        data['ORE'] = 10**12
        if ensure(reactions, data, 'FUEL', mid):
            low = mid
        else:
            high = mid - 1
    return high if ensure(reactions, data, 'FUEL', high) else low


for (test_in, test_out) in TEST_INPUTS:
    print(test_in)
    output = nanofactory(test_in)
    print("expected: ", test_out)
    print("output: ", output)
    assert output == test_out

print(nanofactory(DAY_14_INPUT))
