import requests
import os

HEADER_GET = {
    'X-Unity-Version': '2018.4.7f1',
    'GCA': 'X',
    'Content-Type': 'application/x-www-form-urlencoded',
    'CDNDataVersion': '6310',
    'User-Agent': 'HousamoAPI/4.11.0 Android OS 6.0.1 / API-23 (V417IR/eng.luoweiqiao.20201016.150344)',
    'Response-Crypt': 'enable',
    'Host': 'elb.housamo.jp',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

HEADER_POST = {
    'Expect': '100-continue',
    'X-Unity-Version': '2018.4.7f1',
    'GCA': 'X',
    'Content-Type': 'application/x-www-form-urlencoded',
    'CDNDataVersion': '6310',
    'User-Agent': 'HousamoAPI/4.11.0 Android OS 6.0.1 / API-23 (V417IR/eng.luoweiqiao.20201016.150344)',
    'Response-Crypt': 'enable',
    'Host': 'elb.housamo.jp',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}


def login_by_authkey(auth_key):
    data = {'auth_key': auth_key}

    url1 = 'http://elb.housamo.jp/account/login'
    url2 = f'https://elb.housamo.jp/user/status?auth_key={auth_key}'
    url3 = f'http://elb.housamo.jp/mypage/status?auth_key={auth_key}'

    res1 = requests.post(url1, headers = HEADER_POST, data = data)
    res2 = requests.get(url2, headers = HEADER_GET)
    res3 = requests.get(url3, headers = HEADER_GET)

    print(res1.text, '\n')
    print(res2.text, '\n')
    print(res3.text, '\n')

if __name__ == '__main__':
    AUTH_KEYS = (os.environ["auth_key_gofly"],)
    for auth_key in AUTH_KEYS:
        login_by_authkey(auth_key) 
