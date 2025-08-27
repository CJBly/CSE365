import sys
# Hex-encoded password (as an example)
correct_password = "🙌 🐮 🌔 🔇"

# Step 1: Encode the password in UTF-8 and then convert it to hex
hex_encoded = correct_password.encode("utf-8").hex()
print(f"Hex-encoded password: {hex_encoded}")

# Step 2: Decode the hex-encoded password back to bytes
entered_password = bytes.fromhex(hex_encoded)

# Step 3: Directly decode using 'utf-8' encoding (this is key for emojis and multi-byte characters)
decoded_password = entered_password.decode("utf-8")

# This prints the decoded password in UTF-8 (which should match the original)
print(f"Decoded password: {decoded_password}")
