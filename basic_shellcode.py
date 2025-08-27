from pwn import *
context.clear(arch='amd64')

p = process("/challenge/binary-exploitation-basic-shellcode")

# Raw shellcode bytes
