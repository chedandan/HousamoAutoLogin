import os
import requests

header = {

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

auth_key = os.environ["authkey"]

url = 'http://elb.housamo.jp/user/status?auth_key=' + auth_key
res = requests.get(url, headers = header)
print(res.content)
