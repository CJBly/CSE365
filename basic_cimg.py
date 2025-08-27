with open('file.cimg', 'wb') as t:
    t.write((b"cIMG"))
    #t.write((1920).to_bytes(2, byteorder = "little"))
    t.write((2).to_bytes(2, byteorder = "little"))
    t.write((43).to_bytes(1, byteorder = "little"))
    t.write((23).to_bytes(8, byteorder = "little"))
    
    t.write((b"\x8C\x1D\x40A"*(4*43 * 23)))
