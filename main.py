def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_letters(password):
    return any(symbol.isalpha() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def is_very_long(password):
    return len(password) > 12


def has_symbols(password):
    return any(len(password) > 0 and not symbol.isalpha() and not symbol.isdigit() for symbol in password)


def main():
    password = input('Введите пароль: ')
    password_raiting = [
        has_digit(password),
        has_letters(password),
        is_very_long(password),
        has_lower_letters(password),
        has_upper_letters(password),
        has_symbols(password)
    ]
    score = 0
    for points in password_raiting:
        if points:
            score = score + 2
    print(score)


if __name__ == '__main__':
    main()



