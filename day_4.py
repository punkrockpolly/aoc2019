TEST_INPUTS = [
    (111123, True),
    (111111, True),
    (223450, False),
    (123789, False),
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


def secure_container():
    count = 0

    for i in range(231832, 767346):
        count += validate_password(i)

    return count


for (test_in, test_out) in TEST_INPUTS:
    assert validate_password(test_in) == test_out

print(secure_container())
