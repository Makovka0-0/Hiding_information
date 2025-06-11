import random
from sympy import isprime, mod_inverse #isprime для проверки простоты числа и mod_inverse для нахождения обратного элемента по модулю

#случайное простое число заданной длины в битах
def generate_prime(length: int):
    while True:
        number = random.getrandbits(length)
        if isprime(number):
            return number
#пара ключей для шифрования и расшифрования
def generate_key(length):
    p = generate_prime(length)
    q = generate_prime(length)
    n = p * q
    phi = (p - 1) * (q - 1)
    # Выбираем открытый ключ e
    e_array = [65537, 257, 17]
    e = e_array[0]
    for i in range(3):
        if phi <= e:
            e = e_array[i]
        else: break
    d = mod_inverse(e, phi) #закрытый ключ, который является мультипликативным обратным к e по модулю φ(n)
    # Возвращаем пару ключей
    return [(e, n), (d, n)] # (объединенный открытый ключ, объединенный закрытый ключ)

# Шифрование
def encrypt(public_key, text):
    e, n = public_key
    # Преобразуем строку в число
    plaintext_as_number = int.from_bytes(text.encode(), 'big')
    ciphertext = pow(plaintext_as_number, e, n)
    return ciphertext

# Расшифрование
def decrypt(private_key, text):
    d, n = private_key
    plaintext_as_number = pow(text, d, n)
    # Преобразуем число обратно в строку
    plaintext = plaintext_as_number.to_bytes((plaintext_as_number.bit_length() + 7) // 8, 'big').decode()
    return plaintext