cipher = input("Enter Ciphertext: ").lower()

top = int(input("Top Results: "))

for key in range(top):
    plain = ""

    for ch in cipher:
        if ch.isalpha():
            plain += chr((ord(ch)-97-key)%26+97)
        else:
            plain += ch

    print("Key", key, ":", plain)
