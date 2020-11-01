import rabinMiller, cryptomath, random


def generateKey(keySize):

    p = rabinMiller.generateLargePrime(keySize)

    q = rabinMiller.generateLargePrime(keySize)
    n = p * q

    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    return (publicKey, privateKey)