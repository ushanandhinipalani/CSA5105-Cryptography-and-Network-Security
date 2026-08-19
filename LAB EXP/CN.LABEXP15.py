# Letter Frequency Attack on Caesar Cipher

cipher = input("Enter Ciphertext: ").lower()
top = int(input("Number of possible plaintexts: "))

results = []

for key in range(26):
    plain = ""
    for ch in cipher:
        if ch.isalpha():
            plain += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            plain += ch
    results.append((key, plain))

print("\nPossible Plaintexts:")
for i in range(min(top, 26)):
    print("Key", results[i][0], ":", results[i][1])
