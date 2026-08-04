# RSA Key Regeneration Check

n = 3599
old_e = 31
old_d = 3031

new_e = 17
new_d = 2453

print("Old Public Key :", (old_e, n))
print("Old Private Key:", (old_d, n))

print("\nNew Public Key :", (new_e, n))
print("New Private Key:", (new_d, n))

print("\nUsing the same modulus (n) is NOT secure.")
print("Generate a new modulus with new prime numbers.")
