# Diffie-Hellman Key Exchange

q = 23
a = 5

xa = 6
xb = 15

A = pow(a, xa, q)
B = pow(a, xb, q)

KA = pow(B, xa, q)
KB = pow(A, xb, q)

print("Alice Sends:", A)
print("Bob Sends:", B)

print("Shared Key (Alice):", KA)
print("Shared Key (Bob):", KB)
