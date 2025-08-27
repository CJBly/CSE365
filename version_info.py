with open('file.cimg', 'wb') as t:
    t.write((b"c/Mg"))
    t.write((209).to_bytes(2, byteorder = "little"))
