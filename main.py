PASSWORD = input('Введите пароль: ')

PASSWORD_LIST = list(PASSWORD)


def has_digit(PASSWORD):
    return any(symbol.isdigit() for symbol in PASSWORD_LIST)


def has_letters(PASSWORD):
    return any(symbol.isalpha() for symbol in PASSWORD_LIST)


def has_upper_letters(PASSWORD):
    return any(symbol.isupper() for symbol in PASSWORD_LIST)


def has_lower_letters(PASSWORD):
    return any(symbol.islower() for symbol in PASSWORD_LIST)


def is_very_long(PASSWORD):
    return len(PASSWORD) > 12


def has_symbols(PASSWORD):
    return any(len(PASSWORD) > 0 and not symbol.isalpha() and not symbol.isdigit() for symbol in PASSWORD_LIST)


def main():
    password_raiting = [
        has_digit(PASSWORD),
        is_very_long(PASSWORD),
        has_lower_letters(PASSWORD),
        has_upper_letters(PASSWORD),
        has_symbols(PASSWORD)
    ]

    score = 0

    for points in password_raiting:
        if points:
            score = score + 2

    print(score)


if __name__ == '__main__':
    main()
