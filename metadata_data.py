with open('file.cimg', 'wb') as t:
    t.write((b"{m6e"))
    #t.write((1920).to_bytes(2, byteorder = "little"))
    t.write((1).to_bytes(2, byteorder = "little"))
    t.write((63).to_bytes(4, byteorder = "little"))
    #t.write((0).to_bytes(3, byteorder = "little"))
    t.write((22).to_bytes(8, byteorder = "little"))
    #t.write((0).to_bytes(7, byteorder = "little"))
    t.write((0).to_bytes(63*22, byteorder = "little"))
