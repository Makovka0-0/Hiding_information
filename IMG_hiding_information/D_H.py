from random import randint

def generate_key_close():
    key = randint(10000000, 99999999)
    return key

def create_key_open_close(g, p):
    key_close = generate_key_close()
    key_open = pow(g, key_close, p)
    return [key_open, key_close]

def create_key_common(key_open, key_close, p):
    key = pow(key_open[0], key_close[1], p)
    return key
