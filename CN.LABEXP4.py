text = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()

cipher = ""
j = 0

for ch in text:
    if ch.isalpha():
        shift = ord(key[j % len(key)]) - ord('A')
        cipher += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        j += 1
    else:
        cipher += ch

print("Ciphertext:", cipher)
