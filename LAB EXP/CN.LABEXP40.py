from collections import Counter

cipher = input("Enter Ciphertext: ").upper()

top = int(input("Top Results: "))

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

freq = Counter(cipher)

cipher_order = ''.join(x[0] for x in freq.most_common())

mapping = {}

for i in range(min(len(cipher_order), len(english))):
    mapping[cipher_order[i]] = english[i]

plain = ""

for ch in cipher:
    if ch.isalpha():
        plain += mapping.get(ch, ch)
    else:
        plain += ch

for i in range(top):
    print("Result", i+1)
    print(plain)
