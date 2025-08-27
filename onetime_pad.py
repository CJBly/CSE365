import sys
import base64
from Crypto.Util.strxor import strxor

cipher = bytes.fromhex("831666b048252211a1075ff28c8b93cb6c2931662ed2f34882334791eaa9d5ab62ec2c1d2efec845efd2c8b8da6e5cf7da6848738ea2c2b7fe7d")
key = bytes.fromhex("b22049df6a0b0f3c85217bc8bea6a2be1c2e0a6a2babf06ca1174fb7f4bbb9de5afa0b3330ebcc2acac5f3b7e16259faaa4a4d7ffe88f9a1c236")
plain = (strxor(cipher,key))
print(plain)
flag = (strxor(plain, bytes.fromhex("41") * len(cipher)))
print(flag)
