up_alph = {
    0: 'А',
    1: 'Б',
    2: 'В',
    3: 'Г',
    4: 'Д',
    5: 'Е',
    6: 'Ё',
    7: 'Ж',
    8: 'З',
    9: 'И',
    10: 'Й',
    11: 'К',
    12: 'Л',
    13: 'М',
    14: 'Н',
    15: 'О',
    16: 'П',
    17: 'Р',
    18: 'С',
    19: 'Т',
    20: 'У',
    21: 'Ф',
    22: 'Х',
    23: 'Ц',
    24: 'Ч',
    25: 'Ш',
    26: 'Щ',
    27: 'Ъ',
    28: 'Ы',
    29: 'Ь',
    30: 'Э',
    31: 'Ю',
    32: 'Я'
}

low_alph = {
    0: 'а',
    1: 'б',
    2: 'в',
    3: 'г',
    4: 'д',
    5: 'е',
    6: 'ё',
    7: 'ж',
    8: 'з',
    9: 'и',
    10: 'й',
    11: 'к',
    12: 'л',
    13: 'м',
    14: 'н',
    15: 'о',
    16: 'п',
    17: 'р',
    18: 'с',
    19: 'т',
    20: 'у',
    21: 'ф',
    22: 'х',
    23: 'ц',
    24: 'ч',
    25: 'ш',
    26: 'щ',
    27: 'ъ',
    28: 'ы',
    29: 'ь',
    30: 'э',
    31: 'ю',
    32: 'я'
}


def shifr(input_string, shift_key):
    sh = ''
    for i in input_string:
        if i == 'ё':
            sh += low_alph.get((ord(i) + (shift_key + 21) - ord('a')) % 33)

        elif i == 'Ё':
            sh += up_alph.get((ord(i) + (shift_key + 21) - ord('А')) % 33)

        elif ord(i) >= 1078:
            sh += low_alph.get((ord(i) + (shift_key + 1) - ord('а')) % 33)

        elif 1046 <= ord(i) < 1072:
            sh += up_alph.get((ord(i) + (shift_key + 1) - ord('А')) % 33)

        elif i.isupper() and i.isalpha() and i in up_alph.values():
            sh += up_alph.get((ord(i) + shift_key - ord('А')) % 33)

        elif i.lower() and i.isalpha() and i in low_alph.values():
            sh += low_alph.get((ord(i) + shift_key - ord('а')) % 33)
        else:
            sh += i
    return sh




def rasshifr(zash_str, shift_key):
    rassh = ''
    for i in zash_str:
        if i == 'ё':
            rassh += low_alph.get((ord(i) - (shift_key + 12) - ord('a')) % 33)
        elif i == 'Ё':
            rassh += up_alph.get((ord(i) - (shift_key + 12) - ord('А')) % 33)

        elif ord(i) >= 1078:
            rassh += low_alph.get((ord(i) - (shift_key - 1) - ord('а')) % 33)

        elif 1046 <= ord(i) < 1072:
            rassh += up_alph.get((ord(i) - (shift_key - 1) - ord('А')) % 33)

        elif i.isupper() and i.isalpha() and i in up_alph.values():
            rassh += up_alph.get((ord(i) - shift_key - ord('А')) % 33)
        elif i.lower() and i.isalpha() and i in low_alph.values():
            rassh += low_alph.get((ord(i) - shift_key - ord('а')) % 33)
        else:
            rassh += i
    return rassh


