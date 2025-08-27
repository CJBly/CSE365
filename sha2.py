import hashlib
import os
import base64

challenge_b64 = "aLF8+5b4CiYGRtKaCwxdMvd1TH5Jwn4Ogue/prcbsJY="
challenge_bytes = base64.b64decode(challenge_b64)
attempts = 0
prefix = b'\x00\x00'
while True:
    test_in = os.urandom(8)
    test_hash = hashlib.sha256(challenge_bytes+test_in).digest()
    print(f"{attempts}")
    if test_hash[:2] == prefix:
        response_b64 = base64.b64encode(test_in).decode()
        print(f"Collision found after {attempts} attempts!")
        print(f"Colliding Input (hex): {response_b64}")
        break
    attempts += 1
