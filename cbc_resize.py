import sys
import base64
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES
import requests
from binascii import unhexlify, hexlify
from Crypto.Util.Padding import pad
task = ("a44b69a57d79df73aa6b73b0b9162dfabf588e5c6e9662bb99631d62cc4fb688")
task_bytes = unhexlify(task)
iv = task_bytes[:16]
cipher = task_bytes[16:]
original = pad(b"sleep", 16)
print(original)
target = b"flag" + b"\x0c"*12
print(target)
z = strxor(original,target)
new_iv = bytearray(iv)
new_iv[:16] = strxor(iv[:16], z[:16])
#new_iv = new_iv[4].strip()
#new_iv[4] ^= 0x7b
# var = 0x61
# var ^= 0x0b^0x0c
# print(var)
print(new_iv)
new_task = bytes(new_iv) + cipher
flag = hexlify(new_task)
print(flag)
print("TASK: ", hexlify(new_task).decode())
