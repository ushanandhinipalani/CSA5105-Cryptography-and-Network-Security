# DES Decryption Key Schedule

keys = []

for i in range(1, 17):
    keys.append("K" + str(i))

print("Encryption Keys:")
print(keys)

print("\nDecryption Keys:")
print(list(reversed(keys)))
