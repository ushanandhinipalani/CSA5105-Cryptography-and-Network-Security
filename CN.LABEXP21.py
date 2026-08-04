# Padding Demonstration

msg = input("Enter Message: ")

block = 8

pad = block - (len(msg) % block)

if pad == block:
    pad = block

msg = msg + ('1' + '0' * (pad - 1))

print("Padded Message:", msg)
print("Length:", len(msg))
