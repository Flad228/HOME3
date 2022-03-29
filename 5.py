from random import choice


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def gen(from_, used_, unique):
    while True:
        n_nouns = choice(from_)

        if not (unique and n_nouns in used_):
            used_.append(n_nouns)
            break

    return (n_nouns, used_)