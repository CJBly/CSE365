import base64
from Crypto.PublicKey import RSA

key = RSA.generate(1024)

e = key.e
n = key.n
d = key.d

print(f"e: {hex(e)}")
print(f"n: {hex(n)}")

#challenge_in = int(input("challenge: "), 16)
#response = pow(challenge_in, key.d, n)
print(f"d: {hex(d)}")
#print(f"response: {hex(response)}")
cipher_base64 = "TKDB9oEQq81dVURERDvBh30p68JyxCSbeQGIvO2p1gHF/sjvp7yD9qguNrNh7n3ELvWl3kIOLIlSWsJdST2TkXVQWHrKtukDdYUhE1zOiNVPo/U2HUekU1RquBpR5zn/kfOMZxYECo4Gg/8fXOsdUB+6RopzQNKeaIYf0MSMCTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
cipher_bytes = base64.b64decode(cipher_base64)
cipher_int = int.from_bytes(cipher_bytes,"little")
eVal = int("0x10001", 16)
nVal = int("0xd77135f2677313e5cc00046d8f53b768575188b5994da0917bc8387dac541428d9dd7c28d50219be8b55768077823d3f265a4bbf749e74a7d67051e67852c40906183d69f4e80dca078b5b606d9394617a0a19f993c672f3615c9b79a96b8dc2dcc3b2651d471a1ab7e5668111adb0874e93d43fad5d8e89881eb2a6bbc4bc6f", 16)
dVal = int("0x2d9c9f5241caa054cf7ad575289a0dc37e7119a370e0797533a2b12b1237fec8a34f7c00dd1003c94e907a753a580d85782637d141ec66403e6b2b3bc30faac6e68c97a7ed8f9f7d21dfa82fa51a53ad6eb335c4e7ec793bc13bf7490234c02336c9c2f04768c675231a43e1e0207fe85e62e305aeac15285c9b1958d4b9ee09", 16)
decrypted = pow(cipher_int, dVal, nVal).to_bytes(256, "little")
print(decrypted)
