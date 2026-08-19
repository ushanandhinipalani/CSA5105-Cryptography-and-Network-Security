from math import gcd

text = input("Enter plaintext: ").upper()
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if gcd(a, 26) != 1:
    print("Invalid value of a! Choose a value coprime with 26.")
else:
    cipher = ""
    for ch in text:
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            cipher += chr(c + ord('A'))
        else:
            cipher += ch

    print("Ciphertext:", cipher)
