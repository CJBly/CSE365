from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

p = process("/challenge/run")
possible = "1234567890qwertyuiopasdfghjklzxcvbnm.-_{}QWERTYUIOPASDFGHJKLZXCVBNM"
flag = ""
length = 0
temp = ""
encrypted = ""
block_size = 16
a = 0
b = 32
first_block = True
second_block = False
last_byte = False
for blocks in range(4):
    prefix = b"0" * 15
    for j in range(16):
        #print(length)
        p.recvuntil(b"Data?")

        p.sendline(prefix.hex())
        #print("Flag Block: " + prefix.hex())
        p.recvuntil("Ciphertext: ")

        temp = p.recvline().decode().strip()[a:b]
        #print("Flag encrypt: " + temp)
        #prefix -= b"0"

        for i in range(33, 132):
            #print(length)
            if length == 14:
                last_byte = True
            if length == 15:
                last_byte = False
            p.recvuntil(b"Data?")
            p.sendline(prefix.hex() + flag.encode().hex() + chr(i).encode().hex())
            #print("Possible Flag: " + prefix.hex() + flag.encode().hex() +chr(i).encode().hex())
            p.recvuntil("Ciphertext: ")
            encrypted = p.recvline().decode().strip()[a:b]
            #print("Possible encrypt: " + encrypted)
            #print(temp[:32])
            #print(encrypted[:32]) 
            if encrypted == temp:

                flag += chr(i)
                length = length + 1
                print(length)
                print(flag)
                break
        prefix = b"0"*(15-length) #shorten prefix by 1
        print({prefix})
        #at multiple of 16, when the block reaches 0 , we reset the block to 15 and look at the second block instead of [:16]
    print(f"flag = {flag}")

    a += 32
    b += 32
    length = 0
