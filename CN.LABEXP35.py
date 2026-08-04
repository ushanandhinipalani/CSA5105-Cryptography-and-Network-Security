plaintext = input("Enter Plaintext: ").replace(" ","").lower()

key = list(map(int,input("Enter Key Stream: ").split()))

cipher = ""

for i in range(len(plaintext)):
    p = ord(plaintext[i]) - 97
    c = (p + key[i]) % 26
    cipher += chr(c + 97)

print("Ciphertext:", cipher)
