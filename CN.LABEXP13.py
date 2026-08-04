# Hill Cipher - Known Plaintext Attack

# Plaintext matrix (HELL)
P = [[7, 4],
     [11, 11]]

# Corresponding Ciphertext matrix (POTH)
C = [[15, 14],
     [19, 7]]

# Function to find modular inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1

# Determinant of plaintext matrix
det = (P[0][0]*P[1][1] - P[0][1]*P[1][0]) % 26
det_inv = mod_inverse(det, 26)

if det_inv == -1:
    print("Plaintext matrix is not invertible.")
else:
    # Adjoint matrix
    adj = [[P[1][1], -P[0][1]],
           [-P[1][0], P[0][0]]]

    # Inverse of plaintext matrix modulo 26
    P_inv = [[(det_inv * adj[i][j]) % 26 for j in range(2)] for i in range(2)]

    # Recover key: K = C × P⁻¹ (mod 26)
    K = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            K[i][j] = (C[i][0] * P_inv[0][j] + C[i][1] * P_inv[1][j]) % 26

    print("Recovered Key Matrix:")
    for row in K:
        print(row)
