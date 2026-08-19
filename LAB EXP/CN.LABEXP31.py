# CMAC Subkey Generation

L = int(input("Enter 64-bit value (decimal): "))

# Left Shift
K1 = L << 1

# Constant for 64-bit block
Rb = 0x1B

if (L >> 63) & 1:
    K1 ^= Rb

K2 = K1 << 1

if (K1 >> 63) & 1:
    K2 ^= Rb

print("Subkey K1 =", K1)
print("Subkey K2 =", K2)
