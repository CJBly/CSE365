with open('file.cimg', 'wb') as t:
    t.write((b"cIMG"))
    #t.write((1920).to_bytes(2, byteorder = "little"))
    t.write((1).to_bytes(2, byteorder = "little"))
    t.write((78).to_bytes(4, byteorder = "little"))
    t.write((12).to_bytes(2, byteorder = "little"))
    t.write((b"I"*(78*12)))
