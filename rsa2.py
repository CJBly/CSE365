import base64
import binascii
from Crypto.Util.number import inverse
def decryption(ciphertext, dhex, nhex):
    decrypted = pow(ciphertext, dhex, nhex)
    print(decrypted)
    decrypted_bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder="little")
    print(decrypted_bytes)
    input()
    #if decrypted_bytes[0] == 0:
       # decrypted_bytes = decrypted_bytes.split(b'\x00', 1)[1]
    return decrypted_bytes
pVal = "0xbbbdb08277ff2bb7fbd38f5ba150f32f3a62bd4ad8c062d483427895807172c9fce19fba1808a79b574eb7a045cef572b02cbd012c416e562b64de2d3cfbf35065e2ceaf1e0af6a9298f982576229e57fbb919bd5584d9720116fb7d7ec4eebdb4efa4cb1c4a2c7a04da9d33619db1f2b6647443a8047a3cf5a28aec4b27317d"
ciphertext = "96f84ee28e731bdc09f5e35cf9839ec7b7f127a6f59f8c4d56ae75fd20cbd6ffe931f110329be7ed6ad98a20a3ad266106577cc77f778eb4b9db7462a2038a9ca1f3c3270a8e8b2f1dc7f12dd7bbbd597874b9acf2224b71b05a6c3b962b9545f41e4216d030d353f098ef0c6b9518282b24d0490f34842a4e73bbb46bceb9321346cd872ee9b4d1c45a9b06da044bd2de6a696025901a7b62ca788efc56fb110680a8d199e5bf143d29802229333df3095931aae602078c35012601960fae2dbbac5ece175899e49391614949522d3bf7054b28ab76377ab5c8e77049d27bcc4f0ea39b83e61182d3bb58ee9e65dafa3759a7683d460e73f52c423019d64011"
qVal = "0xe7a94222b83d4f142cb076cadb0b00a6990fbc7c3238ada56340624999453cec78a407319d0ccf3e1e9da161301e5c7fef8a5cdada894695477fe1e73cb5c386966488c1d73674e850db801e7f2fd4204292e2fb1960b2c25827273be0ef2f8e13a8442ceb3ecfa01c32f2e5955b103378ff6d1d1a27bb7565ccbb0aab94a619"
eVal = 0x10001
phex = int(pVal,16)
qhex = int(qVal,16)
n = phex*qhex
phin = (phex-1)*(qhex-1)
inverse_n = inverse(eVal, phin)
#ehex = int(eVal,16)
cipherhex = bytes.fromhex(ciphertext)
cipherInteger = int.from_bytes(cipherhex, byteorder="little")
#nhex = bytes.fromhex(nVal)
#nInteger = int.from_bytes(nhex, byteorder="little")
#dhex = bytes.fromhex(dVal)
#dInteger = int.from_bytes(dhex, byteorder="little")
decrypted = pow(cipherInteger, inverse_n, n)
decrypted_bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder="little")
print(decrypted_bytes.decode())
