import secrets
import requests
from bs4 import BeautifulSoup
import time
for i in range(10):

    url  = "http://127.0.0.1:5000/"
    """  اوامر ثابته ومعتمدة """
    req_token = requests.get(url)#
    print(req_token.text)
    soup_scarper = BeautifulSoup(req_token.text,"html5lib")
    """  اوامر ثابته ومعتمدة """
        
    token = soup_scarper.find('input', {'name':'csrf_token'})["value"]

    data = {"username":"admin","password":"123123","csrf_token":token,'submit':"Login",'remember':'y'}

    headers = {
        'Cookie':f'x-csrf_token{token};session={req_token.cookies["session"]}',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    }

    r = requests.post(url,data=data,headers=headers,allow_redirects=True)
    if ("/logout") in r.text:
        print('[+] LOG IN SUCCESSEFULY [+]')


