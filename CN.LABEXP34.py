msg = input("Enter Message: ")

block = 8

pad = block - (len(msg) % block)

if pad == block:
    pad = block

msg += '1'
msg += '0' * (pad - 1)

print("Padded Message:", msg)
print("Length:", len(msg))
