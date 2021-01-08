import rsa


def decrypt():
    try:
        primeList = rsa.PrimeGen(100)
        possibleKeys = []
        for p in primeList:
            for q in primeList:
                n = p * q
                if n == publicKey[1]:
                    myTuple = (p, q)
                    possibleKeys.append(myTuple)
        for x in possibleKeys:
            p, q = x
            phi = (p - 1) * (q - 1)
            d = rsa.multiplicative_inverse(publicKey[0], phi)
            possibleKey = (d, p * q)
            decryption = rsa.decrypt(possibleKey, ciphertext)
            if decryption.startswith("h"):
                print("Private key (d, n):")
                print(f"({d}, {p*q})")
                print(decryption)
                break

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    publicKey = (29815, 100127)  # (e, n)
    ciphertext = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186,
                  5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744,
                  81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174,
                  65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934,
                  21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
    decrypt()
