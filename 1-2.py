num_dikt = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четире", "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять"}


def num_translate(num_word):
    return num_dikt.get(num_word)


def num_translate_adv(num_word):
    to_key = num_dikt.get(num_word.lower())

    if to_key:
        return to_key.capitalize() if num_word[0].isupper() else to_key

    return None