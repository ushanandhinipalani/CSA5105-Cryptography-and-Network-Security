import math

# Total possible Playfair keys (25 letters, I/J combined)
total_keys = math.factorial(25)
power1 = math.log2(total_keys)

# Effectively unique keys (divide by 2 because a key and its transpose
# produce the same encryption)
unique_keys = total_keys // 2
power2 = math.log2(unique_keys)

print("Total Playfair keys :", total_keys)
print("Approximate = 2^{:.2f}".format(power1))

print("\nEffectively unique keys :", unique_keys)
print("Approximate = 2^{:.2f}".format(power2))
