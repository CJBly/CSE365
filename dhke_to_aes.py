import secrets
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
p = "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca18217c32905e462e36ce3be39e772c180e86039b2783a2ec07a28fb5c55df06f4c52c9de2bcbf6955817183995497cea956ae515d2261898fa051015728e5a8aacaa68ffffffffffffffff"
p = int(p,16)
g = "0x2"
g = int(g,16)
b = 1234567890
A = "0xc5bdf34847a8a2b6689aeffbfdb9d991608126ad4612fe2a58f01b3fa00bf5f829f9a6ae6967eecc4d54bb2d3c264f12fb7bc9ce33566b386cd10fbda86989c84fa1de770e6be0d7e61a19422670b2c790643feebcda54696c96f75d13809b0ae79dfe8f77440697599bc788f23b316079be03de56eb6a8794a93b5b87223282c5cc2bd0840cc946af78af5fdab55b683ce8aa6f9cc64ef68abd31a979d9563380743c2ed0122d59d9a179ee58d1eb4164855543830979305e736daca348ac8d7d69b9af773f88541f1c8429ff2024a7d64579715931bf467e874b56d377d9c7e002b9d2b76ec3383934efb2c5bce044ac1b057b13a93abe34158c508539d5e6"
A = int(A,16)
B = pow(g,b,p)
hex_B = hex(B)
print(f"public key = {hex(B)}")
secret_bob = pow(A,b,p)
print(f"secret = {hex(secret_bob)}")
s = secret_bob
print(f"s: {s}")
key = s.to_bytes(256, "little")[:16]
print(f"key: {key}")
ciphertext = "f05a1d29c041c6a9670e42023de22759383746e6bb5861b41bdfa06619d61908764258fd6b83241ec2b46a0441bae332ed1a22e94b9a43686261d13126735de72a2f6c75b6b08aad6b766c72e5f9dfca"
ciphertext = bytes.fromhex(ciphertext)
print(f"cipher: {ciphertext}")
cipherInteger = int.from_bytes(ciphertext, byteorder="little")
cipher = AES.new(key, AES.MODE_CBC)
decrypt = cipher.decrypt(ciphertext)
print(decrypt)
