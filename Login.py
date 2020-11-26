import requests
import os

header1 = {
    'X-Unity-Version': '2018.4.7f1',
    'GCA': 'X',
    'Content-Type': 'application/x-www-form-urlencoded',
    'CDNDataVersion': '6262',
    'User-Agent': 'HousamoAPI/4.10.2 Android OS 6.0.1 / API-23 (V417IR/eng.luoweiqiao.20201016.150344) Netease MuMu',
    'Response-Crypt': 'enable',
    'Host': 'elb.housamo.jp',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

header2 = {
    'Expect': '100-continue',
    'X-Unity-Version': '2018.4.7f1',
    'GCA': 'X',
    'Content-Type': 'application/x-www-form-urlencoded',
    'CDNDataVersion': '6262',
    'User-Agent': 'HousamoAPI/4.10.2 Android OS 6.0.1 / API-23 (V417IR/eng.luoweiqiao.20201016.150344) Netease MuMu',
    'Response-Crypt': 'enable',
    'Content-Length': '57',
    'Host': 'elb.housamo.jp',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}


def Login(auth_key):
    data = {'auth_key': auth_key}

    url1 = 'http://elb.housamo.jp/user/status?auth_key=' + auth_key
    url2 = 'http://elb.housamo.jp/account/login'
    url3 = 'https://elb.housamo.jp/user/status?auth_key=' + auth_key

    res1 = requests.get(url1, headers=header1)
    res2 = requests.post(url2, headers=header2, data=data)
    res3 = requests.get(url3, headers=header1)

    if(len(res1.content + res2.content + res3.content) != 0):
        print('OK!')

auth_keys = [os.environ["AUTH_KEY_DANDAN"], os.environ["AUTH_KEY_PIPI"]]

for auth_key in auth_keys:
    Login(auth_key) 
