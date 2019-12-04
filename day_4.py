TEST_INPUTS = [
    (111123, True),
    (111111, True),
    (223450, False),
    (123789, False),
]

TEST_INPUTS_PART_2 = [
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


def validate_password(input):
    password = str(input)
    has_repeat = False

    for i in range(6):
        if i == 5:
            if has_repeat:
                return 1
            return 0
        if password[i] == password[i + 1]:
            has_repeat = True
        if password[i] > password[i + 1]:
            return 0


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


def validate_password_part_2(input):
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


def secure_container_part_2():
    count = 0

    for i in range(231832, 767346):
        count += validate_password_part_2(i)

    return count


for (test_in, test_out) in TEST_INPUTS:
    assert validate_password(test_in) == test_out

print(secure_container())


for (test_in, test_out) in TEST_INPUTS_PART_2:
    result = validate_password_part_2(test_in)
    assert result == test_out

print(secure_container_part_2())
