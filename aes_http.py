import sys
import base64
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES
from pwn import *
import requests

request = requests.session()
possible = "1234567890qwertyuiopasdfghjklzxcvbnm.-_{}QWERTYUIOPASDFGHJKLZXCVBNM"
flag = ""
for i in range(1,100):
    response2 = request.get(f"http://challenge.localhost:80/?query=substr(flag, {i}, 1)").text
    response2 = response2.split()
    response2 = response2[22][20:-6]
    for j in possible:
        encoded_j = base64.b64encode(j.encode()).decode()
        response=request.get(f"http://challenge.localhost:80/?query=\"{j}\"").text
        response = response.split()
        response = response[18][20:-6]
        if response == response2:
            flag += j
            print(flag)
print(flag)
