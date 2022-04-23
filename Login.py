import requests
import os, re

UA = 'HousamoAPI/4.12.0 Android OS 6.0.1 / API-23 (V417IR/eng.luoweiqiao.20201016.150344)'

HEADER_GET = {
    'X-Unity-Version': '2018.4.7f1',
    'GCA': 'X',
    'Content-Type': 'application/x-www-form-urlencoded',
    'CDNDataVersion': '6423',
    'User-Agent': UA,
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
    'CDNDataVersion': '6423',
    'User-Agent': UA,
    'Response-Crypt': 'enable',
    'Host': 'elb.housamo.jp',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}

#获取最新版本的HousamoAPI更新User-Agent
res0 = requests.get('http://elb.housamo.jp/gateway/list', headers=HEADER_GET)
UA = 'HousamoAPI/' + res0.headers['ClientVersion'] + ' Android OS 6.0.1 / API-23 (V417IR/eng.luoweiqiao.20201016.150344)'

#登录
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
    auth_keys = eval(os.environ['auth_keys'])
    print(auth_keys)
    pattern = re.compile(r'AUTH_KEY_.*')                #匹配secrets中的auth_key
    for item in auth_keys.keys():
        if pattern.match(item):
            print(item)
            auth_key = auth[item]
            #login_by_authkey(auth_key) 

