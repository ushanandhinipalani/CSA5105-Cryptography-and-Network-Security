import random

message = input("Enter Message: ")

k1 = random.randint(1,100)
k2 = random.randint(1,100)

sig1 = hash(message + str(k1))
sig2 = hash(message + str(k2))

print("Signature 1:", sig1)
print("Signature 2:", sig2)

if sig1 != sig2:
    print("Different Signatures Generated")
