from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import D_H

def create_keys_and_encrypt(text, g, p):
    text = text.encode('utf-8')
    alice_key_open, alice_key_close = D_H.create_key_open_close(g, p)

    bob_key_open, bob_key_close = D_H.create_key_open_close(g, p)

    alice_shared_secret = D_H.create_key_common(bob_key_open, alice_key_close, p)
    bob_shared_secret = D_H.create_key_common(alice_key_open, bob_key_close, p)

    if alice_shared_secret != bob_shared_secret: return False

    key = alice_shared_secret.to_bytes(16, byteorder='big')[:16]

    data = encrypt(text, key)
    return [data, alice_key_open, alice_key_close, bob_key_open, bob_key_close]

def encrypt(text, key):
    text = text.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC)  # Используем режим CBC (Cipher Block Chaining)

    data_padded = pad(text, AES.block_size)  # Добавляем паддинг
    encrypted_data = cipher.encrypt(data_padded)
    return [encrypted_data, cipher]

def decrypt(encrypted_data, cipher, key):
    iv = cipher.iv  # Инициализируем вектор (IV) для CBC режима
    # Дешифрование
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)  # Инициализируем дешифратор с тем же ключом и IV
    decrypted_data = unpad(cipher_decrypt.decrypt(encrypted_data), AES.block_size)
    return decrypted_data

