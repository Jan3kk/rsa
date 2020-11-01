import rng

# Długość klucza podana w bitach.
keys = rng.generateKey(64)

public_key = keys[0][1]
private_key = keys[1][1]
modulus = keys[0][0]
print()


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


message = input("Podaj wiadomość do zaszyfrowania: ")
encrypted = encrypt(message, public_key, modulus)
print("Zaszyfrowana wiadomość: " + encrypted)
print("\nOdszyfrowana wiadomość: " + decrypt(encrypted, private_key, modulus))

# Opis programu:
# Program losowo znajduje 2 liczby pierwsze p i q, oblicza N = p * q, znajduje e, które jest kluczem publicznym oraz
# d, które jest kluczem prywatnym. Pyta nas o wiadomość do zaszyfrowania, a następnie zamienia string na znaki ASCII
# wyrażone w sys. heksadecymalnym, całość łączy i przekształca w liczbę dziesiętną, którą z kolei podaje operacji
# szyfrowania i finalnie zamienia na liczbę hex, która jest naszą zaszyfrowaną wiadomością.
# To samo dzieje się z odszyfrowywaniem, ale w odwrotnej kolejności.
#
# P.S.
# Gdy chcemy wprowadzić dłuższe wiadomości, należy zwiększyć długość klucza.
#
# -------- ŹRÓDŁA --------
# niestety nie potrafiłem stworzyć funkcji szukającej e i d, więc wziąłem ją stąd:
# https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_creating_rsa_keys.htm
# 1* https://www.youtube.com/watch?v=4zahvcJ9glg&t=1s
# 2* https://www.youtube.com/watch?v=oOcTVTpUsPQ&t=1s
# 3* https://pl.wikipedia.org/wiki/RSA_(kryptografia)
