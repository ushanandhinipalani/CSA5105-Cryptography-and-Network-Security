# Character-wise RSA Demonstration

message = input("Enter Message: ").upper()

for ch in message:
    if ch.isalpha():
        print(ch, "=", ord(ch)-65)
