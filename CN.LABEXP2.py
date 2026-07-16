plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM".lower()

text = input("Enter the plaintext: ")
result = ""

for ch in text:
    if ch.islower():
        result += cipher[plain.index(ch)]
    elif ch.isupper():
        result += cipher[plain.index(ch.lower())].upper()
    else:
        result += ch

print("Ciphertext:", result)
