
letter = {
    'ə':'e',
    'ı':'i',
    'ö':'o',
    'ü':'u',
    'ş':'s',
    'ğ':'g',
    'ç':'c',
    ',':'',
    '!':' ',
    '.':' ',
    ' ':'-'
}


def replace_letter(text):
    for key,value in letter.items():
        text = text.replace(key,value)
    return text