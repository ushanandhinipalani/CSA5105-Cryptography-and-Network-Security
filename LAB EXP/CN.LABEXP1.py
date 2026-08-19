text = input("Enter the text: ")
k = int(input("Enter the shift value (1-25): "))

result = ""

for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
    elif ch.islower():
        result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    else:
        result += ch

print("Encrypted text:", result)
