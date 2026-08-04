key = 253

counter = 0

plaintext = [1,2,4]

cipher = []

print("Encryption")

for p in plaintext:
    keystream = counter ^ key
    c = p ^ keystream
    cipher.append(c)
    counter += 1

print("Ciphertext:", cipher)

print("\nDecryption")

counter = 0

plain = []

for c in cipher:
    keystream = counter ^ key
    p = c ^ keystream
    plain.append(p)
    counter += 1

print("Recovered Plaintext:", plain)
