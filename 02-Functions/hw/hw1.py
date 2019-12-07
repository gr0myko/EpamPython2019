def letters_range(*args, **replace_dict):
    if len(args) == 1:
        start, stop, step = 'a', args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise ValueError('letters_range takes 1 - 3 arguments')

    def main_letters_range(start: str, stop: str, step: int, **replace_dict):
        ranged = []
        letter_ord = ord(start.lower())
        if letter_ord < ord(stop.lower()):
            while letter_ord < ord(stop.lower()):
                ranged.append(chr(letter_ord))
                letter_ord += step
        elif letter_ord > ord(stop.lower()):
            while letter_ord > ord(stop.lower()):
                ranged.append(chr(letter_ord))
                letter_ord += step
        for key, value in replace_dict.items():
            for ind, letter in enumerate(ranged):
                if key == letter:
                    ranged[ind] = replace_dict[key]
        return ranged

    return main_letters_range(start, stop, step, **replace_dict)

print(letters_range('g', 'p', 2, **{'l': 7, 'o': 0}))