# ECB Error Propagation Demonstration

plaintext = ["P1", "P2", "P3", "P4"]

print("Original Plaintext Blocks:")
print(plaintext)

ciphertext = ["C1", "C2", "C3", "C4"]

print("\nCiphertext Blocks:")
print(ciphertext)

print("\nAssume C1 contains one bit error.")

print("Recovered Plaintext:")
print("P1 -> Corrupted")
print("P2 -> Correct")
print("P3 -> Correct")
print("P4 -> Correct")
