# CBC Mode Demonstration

plaintext = ["P1", "P2", "P3", "P4"]
iv = "IV"

print("Initialization Vector:", iv)

previous = iv

print("\nEncryption Process")

for i in range(len(plaintext)):
    x = plaintext[i] + " XOR " + previous
    cipher = "Encrypt(" + x + ")"
    print("C{} = {}".format(i+1, cipher))
    previous = "C" + str(i+1)

print("\nDecryption Process")

previous = iv

for i in range(len(plaintext)):
    plain = "Decrypt(C{}) XOR {}".format(i+1, previous)
    print("P{} = {}".format(i+1, plain))
    previous = "C" + str(i+1)
