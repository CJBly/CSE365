import sys
import base64
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES
from pwn import *

p = process("/challenge/run")
def encrypt_chosen(pt):
    p.recvuntil(b"Choice?")
    p.sendline(b"1")
    p.recvuntil(b"Data?")
    p.sendline(pt.encode())
    p.recvuntil(b"Result:")
    ct_b64 = p.recvline().strip()
    return ct_b64

def encrypt_flag(length):
    p.recvuntil(b"Choice?")
    p.sendline(b"2")
    p.recvuntil(b"Index?")
    p.sendline(b"0")
    p.recvuntil(b"Length?")
    p.sendline(str(length).encode())
    p.recvuntil(b"Result:")
    ct_b64 = p.recvline().strip()
    return ct_b64

possible = "1234567890qwertyuiopasdfghjklzxcvbnm.-_{}QWERTYUIOPASDFGHJKLZXCVBNM"
flag = ""
for i in range(1,58):
    for j in possible:
        cipher = flag + j
        if encrypt_chosen(cipher) == encrypt_flag(i):
            flag += j
print(flag)
