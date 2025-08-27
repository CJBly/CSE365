import sys
import base64
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES
aes = bytes.fromhex("b'xb$\xbdhDRhA#F\xee\x96\xd6$\xb0'")
flag = bytes.fromhex("735688d3614966f71ebe602adf30665e2c423a4f32fbd6c8b29204e98c778fb170c96c19df6955f8226133a94479bf3c5ec37734b2270151d5f37b95e7c90bdf13fd485ae6398415576013f968b637a4")
cipher = AES.new(aes, AES.MODE_CBC)
decrypt = cipher.decrypt(flag)
print(decrypt)
