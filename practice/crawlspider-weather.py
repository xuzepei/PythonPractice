#!/usr/bin/env python
#coding=utf-8

import requests
from bs4 import BeautifulSoup

def get_content(url):
    header = {
        'Content-Type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }

    try:
        r = requests.get(url, headers=header, timeout=20)
        print(r.status_code, ":", r.encoding)
        r.encoding = 'UTF8' #设置字符集合
        r.raise_for_status() #抛出异常
    except requests.RequestException as e:
        print(e)
    else:
        return r.text

def parser(text):
    bs = BeautifulSoup(text, "html.parser")
    #print(bs.prettify())

    body = bs.body
    div_7d = body.find('div', {'id': '7d'})
    ul = div_7d.find('ul')
    li_array = ul.find_all('li')

    #print(li_array)

    array = []
    for day in li_array:
        data = {}
        #get date
        date = day.find('h1').string
        data['date'] = date

        #get weather, temperature, wind
        p_array = day.find_all('p')
        #print(p_array)
        for p in p_array:
            if p['class'][0] == 'wea':
                data['weather'] = p.string
            elif p['class'][0] == 'tem':
                #print(p)
                temp1 = p.find('span').string
                temp2 = p.find('i').string
                temp2 = temp2.replace('℃','');
                #temp2 = temp2[:-1]
                #print(len(temp2))
                data['temperature'] = [temp1,temp2]
            # elif p['class'][0] == 'win':
            #     span = p.find('span')
            #     wind_title = span['title']
            #     wind_value = p.find('i').string
            #     data['wind'] = {'title':wind_title, 'value': wind_value}


        array.append(data)

    return array

text = get_content('http://www.weather.com.cn/weather/101190401.shtml')
#parser(text)
print(parser(text))


