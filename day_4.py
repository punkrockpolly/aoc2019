def count_passwords(i):
    count = 0
    password = str(i)
    has_repeat = False

    for i, letter in enumerate(password):
        if i == len(password) - 1:
            if has_repeat:
                count += 1
            break
        if password[i] == password[i + 1]:
            has_repeat = True
        if password[i] > password[i + 1]:
            break

    return count


def secure_container():
    count = 0

    for i in range(231832, 767346):
        count += count_passwords(i)

    return count


print(secure_container())
