#!usr/bin/python3
#coding=utf-8

# import platform
# import ssl
# print("Python info: %s" % (platform.python_version()))
# print("OpenSSL info: %s" % (ssl.OPENSSL_VERSION))

import requests
import json

print(requests.__version__)

def get_content(url):
    header = {
        'Authorization': '12029c611f027fb44111744c05aa085089f4dc6a'
    }

    params = {"per_page": 1, "page": 1}

    try:
        r = requests.get(url, headers=None, params=params, timeout=20)
        if r.status_code == 200:
            r.encoding = 'UTF8' #设置字符集合
        else:
            print(r.status_code, ":", r.encoding)

        r.raise_for_status() #抛出异常
    except requests.RequestException as e:
        print(e)
    else:
        return r.text


#text = get_content2('https://www.howsmyssl.com/a/check')
text = get_content('https://api.github.com/search/repositories?q=player+language:objective-c&sort=stars&order=desc')
parsed = json.loads(text)

if isinstance(parsed, dict):
    print(json.dumps(parsed, indent=4, sort_keys=True))


# print(parsed)
# print(json.dumps(parsed, indent=4, sort_keys=True))


# resp = requests.get('https://api.github.com/search/repositories?q=language:objective-c&sort=stars')
# parsed = json.loads(resp.text)
# print(json.dumps(parsed, indent=4, sort_keys=True))

#resp = requests.get('https://api.github.com/repos/xuzepei/bbc_git/tags')
#print(resp.json())

# resp = requests.get('https://github.stm.com/api/v3/users/octocat/orgs')
# print(resp.text)
#resp = requests.get('https://github.stm.com/api/v3/repos/cd-project-dailycare/ctw0006-unity/tags')
#parsed = json.loads(resp.text)
#print(json.dumps(parsed, indent=4, sort_keys=True))

