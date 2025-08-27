from pwn import *

p = process("/challenge/integration-cimg-screenshot-sc")
magic = p32(0x474D4963)        
version = p16(4)               
num_directives = p32(3)        
padding = b'\x00\x00' 
header = magic + version + num_directives + padding

# Send a valid directive code: 1337 (the special handler)
directive_code = p16(4)
sprite_index_4 = p8(0)
payload_4 = directive_code + sprite_index_4

directive_code2 = p16(5)
x = p8(0)
y = p8(0)
r = p8(255)
g = p8(0)
b = p8(0)
payload_5 = directive_code2 + x + y + r + g + b

directive_code3 = p16(1337)
# Payload for directive 1337:
# Format: index, width, height, row count, column count
sprite_index = p8(0)
width = p8(1)
height = p8(1)
rows = p8(1)
cols = p8(1)
payload_1337 = directive_code3 + sprite_index + width + height + rows + cols

# Final payload
payload = header + payload_1337 + payload_4 + payload_5


p.send(payload)


p.interactive()
#with open('file.cimg', 'wb') as t:
    #t.write((0x474D4963).to_bytes(4, byteorder = "little"))
    #t.write((1920).to_bytes(2, byteorder = "little"))
    #t.write(b"\x04\x00")
    #t.write((1).to_bytes(2, byteorder = "little"))
    #t.write((1).to_bytes(4, byteorder = "little"))
    #.write((1337).to_bytes(2, byteorder="little"))
    #t.write(b"\x00" * 5)
    #t.write(b"\x01\x02\x03\x04\x05")
    #t.write((6).to_bytes(2, byteorder="little"))
    #t.write(b"\x00")
