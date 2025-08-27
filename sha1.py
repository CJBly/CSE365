import hashlib
import os

prefix = "cee197"
attempts = 0
while True:
    test_in = os.urandom(16)
    test_hash = hashlib.sha256(test_in).hexdigest()
    print(f"{attempts}")
    if test_hash[:6] == prefix:
        print(f"Collision found after {attempts} attempts!")
        print(f"Colliding Input (hex): {test_in.hex()}")
        break
    attempts += 1
