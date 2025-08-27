import sys

# The correct password
correct_password = b"ycwxkrqj"

password = "ycwzkrqj"
hex_encoded = ''.join(format(ord(c), '02x') for c in password)
print(hex_encoded)
