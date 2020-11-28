import requests
import os

header_get = {
    'X-Unity-Version': '2018.4.7f1',
    'GCA': 'X',
    'Content-Type': 'application/x-www-form-urlencoded',
    'CDNDataVersion': '6310',
    'User-Agent': 'HousamoAPI/4.10.2 Android OS 6.0.1 / API-23 (V417IR/eng.luoweiqiao.20201016.150344) Netease MuMu',
    'Response-Crypt': 'enable',
    'Host': 'elb.housamo.jp',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

header_post = {
    'Expect': '100-continue',
    'X-Unity-Version': '2018.4.7f1',
    'GCA': 'X',
    'Content-Type': 'application/x-www-form-urlencoded',
    'CDNDataVersion': '6310',
    'User-Agent': 'HousamoAPI/4.10.2 Android OS 6.0.1 / API-23 (V417IR/eng.luoweiqiao.20201016.150344) Netease MuMu',
    'Response-Crypt': 'enable',
    'Content-Length': '57',
    'Host': 'elb.housamo.jp',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}


def Login(auth_key):
    data = {'auth_key': auth_key}

    url1 = 'http://elb.housamo.jp/account/login'
    url2 = 'https://elb.housamo.jp/user/status?auth_key=' + auth_key
    url3 = 'http://elb.housamo.jp/mypage/status?auth_key=' + auth_key

    res1 = requests.post(url1, headers = header_post, data = data)
    res2 = requests.get(url2, headers = header_get)
    res3 = requests.get(url3, headers = header_get)

    print(res1.content, '\n')
    print(res2.content, '\n')
    print(res3.content, '\n')

auth_keys = [os.environ["auth_key_dandan"], os.environ["auth_key_pipi"]]

for auth_key in auth_keys:
    Login(auth_key) 
