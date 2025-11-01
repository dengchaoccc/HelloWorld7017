#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/31 13:06
# @Author  : mac
# @File    : 02_getDoubanFakeUserAgent.py
# @Software: PyCharm
import requests
import fake_useragent

def get_by_fake_agent():
    url = "https://m.douban.com/subject_collection/book_top250"
    user_agent = fake_useragent.UserAgent()

    #使用模拟的代理头，每次都随机生成，这样防止被服务器识别成恶意攻击
    headers = {
        'User-Agent':user_agent.random,
    }
    response = requests.get(url)
    txt = response.text
    with open("douban_fake_agent.html","w", encoding=response.encoding) as f:
        f.write(txt)

get_by_fake_agent()
