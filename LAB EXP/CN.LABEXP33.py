plaintext = input("Enter Plaintext: ")
key = input("Enter Key: ")

cipher = ""

for i in range(len(plaintext)):
    cipher += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))

print("Encrypted Text:", cipher)

plain = ""

for i in range(len(cipher)):
    plain += chr(ord(cipher[i]) ^ ord(key[i % len(key)]))

print("Decrypted Text:", plain)
