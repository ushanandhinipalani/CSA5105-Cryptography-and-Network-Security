def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in matrix and c.isalpha():
            matrix.append(c)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find(mat, ch):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == ch:
                return i, j

key = input("Enter key: ")
text = input("Enter plaintext: ").upper().replace("J", "I").replace(" ", "")

pairs = []
i = 0
while i < len(text):
    a = text[i]
    b = text[i+1] if i+1 < len(text) else "X"
    if a == b:
        b = "X"
        i += 1
    else:
        i += 2
    pairs.append(a + b)

mat = create_matrix(key)

print("\nPlayfair Matrix:")
for row in mat:
    print(*row)

cipher = ""
for p in pairs:
    r1, c1 = find(mat, p[0])
    r2, c2 = find(mat, p[1])

    if r1 == r2:
        cipher += mat[r1][(c1 + 1) % 5]
        cipher += mat[r2][(c2 + 1) % 5]
    elif c1 == c2:
        cipher += mat[(r1 + 1) % 5][c1]
        cipher += mat[(r2 + 1) % 5][c2]
    else:
        cipher += mat[r1][c2]
        cipher += mat[r2][c1]

print("Ciphertext:", cipher)
