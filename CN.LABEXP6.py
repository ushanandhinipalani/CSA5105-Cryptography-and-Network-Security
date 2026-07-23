# Affine Cipher Breaking Program

from math import gcd

# Find modular inverse
def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

# Affine decryption
def decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return None

    plaintext = ""

    for ch in cipher:
        if ch.isalpha():
            x = ord(ch.upper()) - ord('A')
            p = (a_inv * (x - b)) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += ch

    return plaintext

# Ciphertext input
ciphertext = input("Enter Ciphertext: ").upper()

# Frequency assumptions:
# B -> E (4)
# U -> T (19)

C1 = ord('B') - ord('A')   # 1
C2 = ord('U') - ord('A')   # 20
P1 = ord('E') - ord('A')   # 4
P2 = ord('T') - ord('A')   # 19

possible_keys = []

for a in range(1, 26):
    if gcd(a, 26) == 1:
        if ((a * (P2 - P1)) % 26) == ((C2 - C1) % 26):
            b = (C1 - a * P1) % 26
            possible_keys.append((a, b))

print("\nPossible Keys and Plaintexts:\n")

for a, b in possible_keys:
    print("Key (a =", a, ", b =", b, ")")
    print("Plaintext:", decrypt(ciphertext, a, b))
    print()
