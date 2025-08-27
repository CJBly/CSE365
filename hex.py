import sys
import base64
def decode_from_bits(s):
    s = s.decode("latin1")
    assert set(s) <= {"0", "1"}, "non-binary"
    assert len(s) % 8 == 0, "must enter data"
    return int.tobytes(int(s,2), length=len(s) // 8, byteorder= "big")
# Binary string represen
correct_password = "ecdgbwfi"

# Start with the correct password (ASCII)
encoded = correct_password.encode().hex()  # Convert ASCII to hex

# Perform nested encoding in reverse
for _ in range(3):  # 4 total layers, so do this 3 more times
    encoded = encoded.encode().hex()

# Write the final encoded value to 'rb'
with open("rb", "w") as file:
    file.write(encoded)

print(f"Nested encoding written to 'rb': {encoded}") 
