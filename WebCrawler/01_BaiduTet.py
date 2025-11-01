#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/25 11:01
# @Author  : mac
# @File    : 01_BaiduTet.py
# @Software: PyCharm
import time

import requests
import datetime
'''
爬虫步骤：
1，定位url
2，发起requst
3，数据提取
4，数据保存
获取百度的页面
'''
def getBaidu():
    url = "https://www.baidu.com"
    #发送的方式是get，并且填写url
    response = requests.get(url)
    #状态值，会放回服务器的结果，一般是200
    print(f"code = {response.status_code}")
    #如果是图片类型，就要使用response.content
    content = response.text
    now_time = datetime.datetime.now()
    print(response.text)
    print(response.encoding)
    #如果加时间：{now_time:%Y-%m-%d %H:%M:%S}, 这里加入编码很关键，否则全是乱码
    with open(f"baidu.html","w", encoding="ISO-8859-1") as f:
        f.write(content)
        f.close()


#豆瓣必须要加一个请求头才可以
def get_douban():
    url = "https://m.douban.com/subject_collection/book_top250"

    #这些值，可以用浏览器打开页面，然后右键--检查--网络，之后再刷新一下页面即可看见
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://www.douban.com/',}

    response = requests.get(url,  headers=headers)

    txt = response.text
    #now_time = datetime.datetime.now()

    print(response.encoding)
    with open(f"douban.html","w", encoding=response.encoding) as f:
        f.write(txt)
    # 这是try的替代文件在这里已经被自动关闭了，即使上面发生了异常


#getBaidu()
get_douban()