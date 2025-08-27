import base64
def decryption(ciphertext, dhex, nhex):
    decrypted = pow(ciphertext, dhex, nhex)
    print(decrypted)
    decrypted_bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder="little")
    print(decrypted_bytes)
    input()
    #if decrypted_bytes[0] == 0:
       # decrypted_bytes = decrypted_bytes.split(b'\x00', 1)[1]
    return decrypted_bytes
dVal = "0x1c5640cd48a36537a0d16dd7a2d0e22ff80f19ea8a9913ad063a668a5574f515a49d0829af102558bd7628773d9e1eccf51cb562e2c0668cad316d317029a82f14405668b9ea635d13b85f76fc3a7276fb52221fe12557a7191a729e4f5af2bb92f4922225c00b992cde9bef7a6adcc2264ed3464798b094f4fb31c6835a1097f34385b9f557844dea4edf8aef058a99819445525ab26c64e946c101d45b48628b7c98215f6d554c34e81bbc9e4e2e845915cbb632a4ddb0bd469da10064324afb116f0de91b8e247a907be3db2b5d38108a1f7d2a251a0057cbf5934664d525db56a96cf8e61d4935126ba330a58ec0607ba14cf7946a9d275ff9655c856021"
ciphertext = "bdf6e81677898af749284839d71be5e6bd3b5f2173eb963c5f6cc34b126772cb8d606007521cefef735e24b269d343c30069d8c234b5c2a6c2fe99d702fd16b735f84d785613525f0f5ac2cd0b373794e36c1b200115b8e7f8bee0c24e1ae4cd3a888ab55631cdb230213087f43a9e4f9fadae2b1c6521c4de4dbcd3ea84f1c69bea870804c3a6c6f26e44c2226c347ad7883dd6347c1ac8f7fc3b2f3700786a0dc964f6a06ae52c82d7b78cc57ab274c9c79a9ea6238fb2fec8ecdf7ddd481ab6fcc514f8053c467616589c15a6a8b80837cc8e637d898fdc38d458da7db66910e66028521846528e954c042044a1c202b0f7e828305d004dac8c79e663d228"
nVal = "0xb4d74fcb0de91426b4e8802052e8a89ae110bc1a2bd4e15fa3ea839ba76f9c48b36b6966389decad70a6569ec392e3c2023c3928d1e185143c5029d1889e8df1f37ce8a07b53180d12aec769a8056b20fbc5f812b1e33c5692273f4de493a11a0044ff0991d6495a8d63bc037b7030fc2782dd5c3527c1da3f4a06068270d792a0fc3e93584e1aea4619d2f3f9024486b02b1c01fab0e987fb150d83aef5582a55c9ef04fae24b4f3498b06275133f8def3e098d354ab6f99b951b40933c92e2b02af28a0908032f9067753009bfe502a9332fec05be1434066d5a885a6ca6538d2039c104729c699fc7c2e536edcf8b87af7ad53619c5f52f34e090949a7cd9"
eVal = 0x10001
dhex = int(dVal,16)
nhex = int(nVal,16)
#ehex = int(eVal,16)
cipherhex = bytes.fromhex(ciphertext)
cipherInteger = int.from_bytes(cipherhex, byteorder="little")
#nhex = bytes.fromhex(nVal)
#nInteger = int.from_bytes(nhex, byteorder="little")
#dhex = bytes.fromhex(dVal)
#dInteger = int.from_bytes(dhex, byteorder="little")
flag = decryption(cipherInteger, dhex, nhex)
#print(flag.decode('utf-8'))
try:
    flag1 = flag.decode('utf-8')
    print(f"Decrypted Flag: {flag1}")
except UnicodeDecodeError:
    print("Decryption successful, but output is not UTF-8. Raw bytes:")
    print(flag.hex())
