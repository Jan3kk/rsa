import enc_dec.py

# Length in bits as an argument
keys = rng.generateKey(64)

public_key = keys[0][1]
private_key = keys[1][1]
modulus = keys[0][0]

message = input("Message to be encrypted: ")
encrypted = encrypt(message, public_key, modulus)
print("Encrypted message: " + encrypted)
print("\nThe same decrypted message: " + decrypt(encrypted, private_key, modulus))
