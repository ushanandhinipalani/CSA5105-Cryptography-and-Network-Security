# Affine Caesar Cipher

def encrypt(text, a, b):
    cipher = ""

    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - 65
            c = (a * p + b) % 26
            cipher += chr(c + 65)
        else:
            cipher += ch

    return cipher

text = input("Enter Plaintext: ")
a = int(input("Enter a (1,3,5,7,9,11,15,17,19,21,23,25): "))
b = int(input("Enter b: "))

print("Ciphertext:", encrypt(text, a, b))
