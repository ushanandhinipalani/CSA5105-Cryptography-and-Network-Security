import math

n = 3599

plaintext = 61

factor = math.gcd(plaintext, n)

if factor > 1:
    print("Common Factor Found:", factor)
    print("Other Factor:", n // factor)
else:
    print("No Common Factor")
