# Playfair Cipher Decryption
# Keyword: MONARCHY

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key:
        if ch not in used and ch.isalpha():
            used.add(ch)
            matrix.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":   # J omitted
        if ch not in used:
            used.add(ch)
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def decrypt_pair(matrix, a, b):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)

    if r1 == r2:                 # Same row
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]

    elif c1 == c2:               # Same column
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]

    else:                        # Rectangle
        return matrix[r1][c2] + matrix[r2][c1]


# Keyword
keyword = "MONARCHY"

# Generate Playfair matrix
matrix = generate_matrix(keyword)

print("Playfair Matrix:\n")
for row in matrix:
    print(" ".join(row))

ciphertext = ("KXJEYUREBEZWEHEWRYTUHEYFS"
              "KREHEGOYFIWTTTUOLKSYCAJPO"
              "BOTEIZONTXBYBNTGONEYCUZWR"
              "GDSONSXBOUYWRHEBAAHYUSEDQ")

plaintext = ""

for i in range(0, len(ciphertext), 2):
    plaintext += decrypt_pair(matrix,
                              ciphertext[i],
                              ciphertext[i+1])

print("\nCiphertext:")
print(ciphertext)

print("\nDecrypted Plaintext:")
print(plaintext)
