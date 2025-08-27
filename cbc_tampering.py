import sys
import base64
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES
import requests
from binascii import unhexlify, hexlify
task = ("195dcffdd08dcc8ef9b435a822a6cfb8ac46bce1a4bca6a9a513d0ffffe7b820")
task_bytes = unhexlify(task)
iv = task_bytes[:16]
cipher = task_bytes[16:]
original = b"sleep"
target = b"flag!"
z = strxor(original,target)
new_iv = bytearray(iv)
new_iv[:5] = strxor(iv[:5], z)
new_task = bytes(new_iv) + cipher
print("TASK: ", hexlify(new_task).decode())
