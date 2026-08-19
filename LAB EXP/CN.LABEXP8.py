# Monoalphabetic Cipher using Keyword

import string

alphabet = string.ascii_lowercase
keyword = "cipher"

# Generate cipher alphabet
cipher_alphabet = ""

for ch in keyword:
    if ch not in cipher_alphabet:
        cipher_alphabet += ch

for ch in alphabet:
    if ch not in cipher_alphabet:
        cipher_alphabet += ch

print("Plain Alphabet : ", alphabet)
print("Cipher Alphabet:", cipher_alphabet)

# Encryption
plaintext = input("\nEnter Plaintext: ").lower()

ciphertext = ""

for ch in plaintext:
    if ch in alphabet:
        index = alphabet.index(ch)
        ciphertext += cipher_alphabet[index]
    else:
        ciphertext += ch

print("Encrypted Text :", ciphertext)

# Decryption
decrypted = ""

for ch in ciphertext:
    if ch in cipher_alphabet:
        index = cipher_alphabet.index(ch)
        decrypted += alphabet[index]
    else:
        decrypted += ch

print("Decrypted Text :", decrypted)
