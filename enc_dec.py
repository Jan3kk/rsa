import rng


def encrypt(string, public, modulus):
    # dla przejrzystości kodu, szyfrowanie i odszyfrowywanie rozbiłem na kilka linii

    hex_ascii_string = string.encode('utf-8').hex()

    int_ascii_string = int(hex_ascii_string, 16)

    encrypted_int = pow(int_ascii_string, public, modulus)

    encrypted_hex = hex(encrypted_int)[2:]

    return encrypted_hex


def decrypt(string, private, modulus):

    encrypted_hex = string

    encrypted_int = int(encrypted_hex, 16)

    decrypted_int = pow(encrypted_int, private, modulus)

    hex_ascii_string = hex(decrypted_int)[2:]

    final_decrypted_string = bytes.fromhex(hex_ascii_string).decode('ascii')

    return final_decrypted_string

