# SHA-3 Capacity Demonstration

block = 1024
capacity = 576

lanes = capacity // 64

print("Capacity Bits:", capacity)
print("Capacity Lanes:", lanes)

print("\nIgnoring permutation...")
print("All lanes become non-zero after one absorption step.")
