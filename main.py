password = input('Введите пароль: ')

password_list = list(password)


def has_digit(password):
    return any(symbol.isdigit() for symbol in password_list)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password_list)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password_list)


def is_very_long(password):
    if len(password) > 12:
        return True


def has_symbols(password):
    for symbol in password_list:
        if len(password) > 0 and not symbol.isalpha() and not symbol.isdigit():
            return True


password_raiting = [
    has_digit(password),
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
