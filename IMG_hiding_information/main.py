import AES
import writing_to_pixels, encryption_algorithms, RSA, D_H

def main():
    choice = ''
    message_encryption = ''
    name_file = ''
    mode = input("Enter file mode (encrypt, decrypt, create_key): ")
    if mode != "create_key":
        name_file = input("Enter file name: ")
        choice = input("Enter decryption mode (Caesar, Vigenere, RSA, D_H_AES): ")

    if mode == "encrypt":
        message = input("Enter message: ")
        if choice == "Caesar":
            key = int(input("Enter key: "))
            message_encryption = encryption_algorithms.Caesar_cipher(key, message, mode)
        elif choice == "Vigenere":
            key = input("Enter key: ")
            message_encryption = encryption_algorithms.Vigenere_cipher(key, message, mode)
        elif choice == "RSA":
            key = input("Transfer (combined public key, combined private key) in this form (public key, private key, module): ")
            key = key.split()
            for ind in range(len(key)): key[ind] = int(key[ind])
            message_encryption = RSA.encrypt(key, message_encryption)
        elif choice == "D_H_AES":
            choice_2 = input("Generate the key and encrypt the message (1) or just encrypt the message (2): ")
            if choice_2 == "1":
                g = int(input("Enter G (base): "))
                p = int(input("Enter P (module): "))
                message_encryption = AES.create_keys_and_encrypt(message, g, p)
                print(f"Message and cipher, Alice_key_open, Alice_key_close, Bob_key_open, Bob_key_close: {message_encryption}")
                message_encryption = message_encryption[0][0]
            elif choice_2 == "2":
                key = input("Enter key: ")
                message_encryption = AES.encrypt(message, key)
            else:
                print("Mod not found. Try again.")
        writing_to_pixels.stega_encrypt(name_file, message_encryption)
        print("The message is recorded")

    elif mode == "decrypt":
        message_decr = writing_to_pixels.stega_decrypt(name_file)
        message = message_decr[1]
        if message_decr[0] == 0:
            print("There is no message encrypted by this program in the image.")
        else:
            print("This message was recorded in this program")

        if choice == "Caesar":
            key = int(input("Enter key: "))
            message_encryption = encryption_algorithms.Caesar_cipher(key, message,  mode)
        elif choice == "Vigenere":
            key = input("Enter key: ")
            message_encryption = encryption_algorithms.Vigenere_cipher(key, message, mode)
        elif choice == "RSA":
            key = input("Transfer (combined public key, combined private key) in this form (public key, private key, module): ")
            key = key.split()
            for ind in range(len(key)): key[ind] = int(key[ind])
            message_encryption = RSA.decrypt(key, message_encryption)
        elif choice == "D_H_AES":
            key = input("Enter key: ")
            cipher = input("Enter cipher key: ")
            message_encryption = AES.decrypt(message_decr, cipher, key)
        print(f"Received message: {message_encryption}")

    elif mode == "create_key":
        choice = input("Enter encryption mode (RSA, D_H): ")
        if choice == "RSA":
            length = int(input("Enter length of key: "))
            key = RSA.generate_key(length)
            print(f"The key is {key} (combined public key, combined private key)")
        elif choice == "D_H":
            g_p = input("Enter the base and module: ")
            g, p = g_p.split(' ')
            g = int(g)
            p = int(p)

            keys_1 = D_H.create_key_open_close(g, p)
            print(f"The key is {keys_1} (public key, private key)")
            keys_2 = D_H.create_key_open_close(g, p)
            print(f"The key is {keys_2} (public key, private key)")
            key_12 = D_H.create_key_common(keys_1, keys_2, p)
            print(f"The key is {key_12} (common secret)")

if __name__ == '__main__':
    main()
