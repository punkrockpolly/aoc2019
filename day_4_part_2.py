TEST_INPUTS = [
    (112233, 1),
    (111111, 0),
    (123444, 0),
    (223450, 0),
    (123789, 0),
    (111122, 1),
    (113444, 1),
    (123444, 0),
    (123445, 1),
    (123345, 1),
    (113456, 1),
    (133456, 1),
    (134456, 1),
    (134566, 1),
    (222456, 0),
    (122245, 0),
    (123335, 0),
    (123444, 0),
]


def search_for_repeat(input_string):
    zero = input_string[0]
    one = input_string[1]
    two = input_string[2]
    three = input_string[3]
    four = input_string[4]
    five = input_string[5]

    if zero == one and one != two:
        return True
    if zero != one and one == two and two != three:
        return True
    if one != two and two == three and three != four:
        return True
    if two != three and three == four and four != five:
        return True
    if three != four and four == five:
        return True
    else:
        return False


def validate_password(input):
    password = str(input)
    has_good_repeat = search_for_repeat(password)

    for i in range(0, 5):
        if password[i] > password[i + 1]:
            return 0

    return has_good_repeat


def secure_container():
    count = 0

    for i in range(231832, 767346):
        count += validate_password(i)

    return count


for (test_in, test_out) in TEST_INPUTS:
    result = validate_password(test_in)
    assert result == test_out

print(secure_container())
