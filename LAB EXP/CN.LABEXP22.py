# CBC Mode using XOR

iv = 170      # 10101010
key = 253

plaintext = [1, 2, 3, 4]

cipher = []

prev = iv

print("Encryption")

for p in plaintext:
    c = (p ^ prev) ^ key
    cipher.append(c)
    prev = c

print("Ciphertext:", cipher)

print("\nDecryption")

prev = iv

plain = []

for c in cipher:
    p = (c ^ key) ^ prev
    plain.append(p)
    prev = c

print("Recovered Plaintext:", plain)
