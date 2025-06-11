SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def Caesar_cipher(key: int, message: str, mode: str) -> str:
    translated = ''
    for char in message:
        if char in SYMBOLS:
            char_index = SYMBOLS.index(char)

            if mode == "encrypt": char_index += key
            elif mode == "decrypt": char_index -= key

            if char_index >= len(SYMBOLS): char_index -= len(SYMBOLS)
            elif char_index < 0: char_index += len(SYMBOLS)

            translated += SYMBOLS[char_index]
        else:
            translated += char

    return translated

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def Vigenere_cipher(key, message, mode):
    translate = ''

    index_key = 0
    key = key.upper()

    for char in message:
        num = LETTERS.find(char)
        if char in LETTERS:
            if mode == "encrypt":
                num += LETTERS.find(key[index_key])
            if mode == "decrypt":
                num -= LETTERS.find(key[index_key])

            num %= len(LETTERS)
            if char.isupper():
                translate += LETTERS[num].upper()
            elif char.islower():
                translate += LETTERS[num].lower()
            index_key += 1
            index_key %= len(key)
        else:
            translate += char

    return translate