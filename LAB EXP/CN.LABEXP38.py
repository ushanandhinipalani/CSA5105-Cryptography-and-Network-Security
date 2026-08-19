# Known Plaintext Attack

P = [[7,4],
     [11,11]]

C = [[15,14],
     [19,7]]

print("Plaintext Matrix")
for i in P:
    print(i)

print("\nCiphertext Matrix")
for i in C:
    print(i)

print("\nKey can be recovered using")
print("K = C × P^-1 (mod 26)")
