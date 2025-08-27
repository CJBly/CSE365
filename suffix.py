from pwn import *

p = process("/challenge/run")
possible = "1234567890qwertyuiopasdfghjklzxcvbnm.-_{}QWERTYUIOPASDFGHJKLZXCVBNM"
flag = ""
length = 1
temp = ""
encrypted = ""

for j in range(58):
    p.recvuntil(b"Choice? ")
    p.sendline(b"2")
    p.sendline(str(j + 1))
    p.recvuntil(b"Result: ")
    temp = p.recvline().strip().decode()
    
    for i in possible:
        p.recvuntil(b"Choice? ")
        p.sendline(b"1")
        p.recvuntil(b"Data? ")
        p.sendline(str(i) + str(flag))
        p.recvuntil(b"Result: ")
        encrypted = p.recvline().strip().decode()
        if encrypted == temp:
            length = length + 1
            flag = i + flag
            print(flag)
