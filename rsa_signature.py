import sys

from base64 import b64encode, b64decode
n = int(open("/challenge/key-n").read(), 16)
print(f"n: {n}")
flag = b"flag"
int_flag = int(int.from_bytes(flag, "little") / 2)
byte_flag = b64encode(int_flag.to_bytes(256, "little"))
print(f"{byte_flag}")
num = 2
byte_num = b64encode(num.to_bytes(256, "little"))
print(f"{byte_num}")
flag_command = "ZVw4F9LsOT7TbiE+0xuWywaECoovF36eBVOhjB58Cb2cpSPLbdwFpIw8K04dUXN5NrFlpgntHM1YaNmWJ47DOQ7QHS3KGtuNblEZypZ4Dpj6Rd0EyDd8GebbFx1FbhqTpZ1xWxfp2xehYoMpR7t9GPBpw6SEr9J13/35XszDAxA03MzBjh11kinnZtFoYwiDNiADDT5cHQ3IlWevdqOjI6mDwakOJ6OanVTDet/DjKYY9RMNOPcomQqEzzPITUWgDg17wY0efzus+1Z8c6lQBUZJKIrwrYNdAKfi7az62fRS/F9fnsgy+Q5smKIgyYWOtruwAPWAXeECqKJLi47iQw=="
num_command = "cW2MqozYnqxahgsqcHCwCqID6yU+/ZzT5+/ufhohjgnRSZSMlolDOE4kPpkvGMn1wjSzS9C4e6VjtkH7kWz/U5hXpZimlLiJxhn15kOG9o5ylTU7FMkN9reTxfD0n39euSV54ljirYUXWKH3Dntk4CfABW7H9sDRdgvfSxi4OEy8wXBL/VbpO7z7anqmhbG8liT5l2sONiRA6/Sp74HMuZe0UfNaadHSmPqKg87LjbXAkHLhXsezAdhua144DzG1FulUhmmfo/nwBTnLVoUv+zeWqVWC6pgZZH2RBviu/u7uyAQHNdryNowSomOpKunAjVDg5TvP+9a/Abbr6FeGNw=="
flag_command_bytes = b64decode(flag_command)
flag_command_int = int.from_bytes(flag_command_bytes,"little")
num_command_bytes = b64decode(num_command)
num_command_int = int.from_bytes(num_command_bytes,"little")
final_flag = flag_command_int*num_command_int % n
decrypted = b64encode(final_flag.to_bytes(256,"little"))
print(f"{decrypted}")

# print(final_byte_flag)
