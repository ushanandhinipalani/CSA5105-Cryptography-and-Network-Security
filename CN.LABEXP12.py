key = [[9, 4], [5, 7]]

plaintext = "meetmeattheusualplaceattenratherthaneightoclock"
plaintext = plaintext.replace(" ", "").lower()

if len(plaintext) % 2 != 0:
    plaintext += "x"

cipher = ""

for i in range(0, len(plaintext), 2):
    p1 = ord(plaintext[i]) - 97
    p2 = ord(plaintext[i + 1]) - 97

    c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
    c2 = (key[1][0] * p1 + key[1][1] * p2) % 26

    cipher += chr(c1 + 97)
    cipher += chr(c2 + 97)

print("Ciphertext:", cipher)
