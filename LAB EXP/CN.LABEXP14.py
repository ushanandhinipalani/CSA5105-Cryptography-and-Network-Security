plaintext = "sendmoremoney".replace(" ","")
key = [9,0,1,7,23,15,21,14,11,11,2,8,9]

cipher = ""

for i in range(len(plaintext)):
    p = ord(plaintext[i]) - 97
    c = (p + key[i]) % 26
    cipher += chr(c + 97)

print("Ciphertext :", cipher)
