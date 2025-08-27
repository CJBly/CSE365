from pwn import *

p = process("/challenge/run")
possible = "1234567890qwertyuiopasdfghjklzxcvbnm.-_{}QWERTYUIOPASDFGHJKLZXCVBNM"
flag = ""
length = 1
temp = ""
encrypted = ""
block_size = 16
prefix = b"00000000"

for j in range(57):
    
    p.recvuntil(b"Choice? ")
    p.sendline(b"2")
    p.sendline(prefix)
    p.recvuntil(b"Result: ")
    temp = p.recvline().decode().strip()[128:]
    prefix += b"0"

    for i in possible:
        p.recvuntil(b"Choice? ")
        p.sendline(b"1")
        p.recvuntil(b"Data? ")
        p.sendline(i.encode() + flag.encode())
        p.recvuntil(b"Result: ")
        encrypted = p.recvline().decode().strip()
        if encrypted == temp:
            flag = i+ flag
            print(flag)
            break
# for i in range(0, len(flag), 57):
#     print(flag[i])

# prefix = b"A" * 8
# p.recvuntil(b"Choice? ")
# p.sendline(b"2")
# p.sendline(prefix)
# p.recvuntil(b"Result: ")
# temp = bytes.fromhex(p.recvline().strip().decode())[-16:]

# p.recvuntil(b"Choice? ")
# p.sendline(b"1")
# p.recvuntil(b"Data? ")
# p.sendline(b"}")
# p.recvuntil(b"Result: ")
# encrypted = bytes.fromhex(p.recvline().strip().decode())

# print(temp)
# print(encrypted)
