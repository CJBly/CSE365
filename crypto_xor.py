import sys
import base64
#letter = ord('R') #converts ascii to decimal
#print(letter)
#second_num = int("0x63",16) #hex to decimal
#print(second_num)
#final = letter^second_num
#final = chr(final)
#print(final)
from Crypto.Util.strxor import strxor
final = strxor(b"jOcKDEbuIH", b"!$)%)))%$&")
print(final)
