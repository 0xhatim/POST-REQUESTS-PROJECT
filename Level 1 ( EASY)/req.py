import requests
import os

url  = "http://127.0.0.1:5000/"
data = {"username":"admin","password":"123123","csrf_token":os.urandom(91)}

r = requests.post(url,data=data).text

print(r)
