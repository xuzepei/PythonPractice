#!/usr/bin/env python
#coding=utf-8

import requests
import json

def get_content(url):
    header = {
        'Content-Type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }

    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = r'ADMOB=7gXQZR6TDQOOVgxf73MdSwhZV4ExOvpd6aqaLDuP38LQujUEAGFCJtFTcM0Ho-8Y5SVQ4w.; S=ads-app-monetization=e2bmB4JyDleM585BqUYhk8nnR6-RGX15; _ga=GA1.2.1515297777.1522138939; _gid=GA1.2.361670399.1522138939'

    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

    try:
        r = requests.get(url, headers=header, timeout=20, cookies=cookies)
        if r.status_code == 200:
            r.encoding = 'UTF8' #设置字符集合
        else:
            print(r.status_code, ":", r.encoding)

        r.raise_for_status() #抛出异常
    except requests.RequestException as e:
        print(e)
    else:
        return r.text

text = get_content('https://apps.admob.com/#home')
print(text)