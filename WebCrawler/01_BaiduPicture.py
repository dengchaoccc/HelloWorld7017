#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/28 16:48
# @Author  : mac
# @File    : 01_BaiduPicture.py
# @Software: PyCharm
#使用爬虫获取百度的图片
import  requests
def get_image_from_Baidu():
    url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"

    rsp = requests.get(url)
    if rsp.status_code == 200:
        print("now recieved code 200, result is OK")

    content = rsp.content

    with open("baidu.png","wb") as f:
        f.write(content)
        f.close()

get_image_from_Baidu()