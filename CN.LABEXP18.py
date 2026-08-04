# DES Subkey Demonstration

key = input("Enter 56-bit key (binary): ")

left = key[:28]
right = key[28:]

print("Left 28 bits :", left)
print("Right 28 bits:", right)

print("\nSubkey Generation")

for i in range(1, 17):
    left = left[1:] + left[0]
    right = right[1:] + right[0]

    subkey = left[:24] + right[:24]

    print("K{} = {}".format(i, subkey))
