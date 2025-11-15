#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/13 11:12
# @Author  : mac
# @File    : 11_TimeRelated.py
# @Software: PyCharm
import time
from datetime import datetime

def time_demo():
    c_time = time.ctime()
    print(f"ct-time = {c_time}")

    local_time = time.localtime()
    print(f"local time = {local_time}")

def date_time_demo():
    now_time = datetime.now()
    print(f"now time = {now_time}")
    time.sleep(10)
    now_time = datetime.now()
    print(f"after 10s , not the time is {now_time}")

    #打印当前格式：
    print(f"当前时间: {now_time.strftime('%Y年%m月%d日 %H:%M:%S')}")

def time_counter():
    try:
        #做一个简单的计时器
        start_flag  = input("输入任何非空按钮开始计时")
        start_time = datetime.now()
        while True:
            now_time = datetime.now()
            print(f"\r{now_time.strftime('%H:%M:%S')}")
            #print(f"\r{time.time():.1f}") #打印浮点数，保留1位小数
            time.sleep(1)

    except  KeyboardInterrupt :
        end_time = datetime.now()
        time_gap = end_time - start_time
        #小数点截断方法：  = float(f"{x:.2f}")  # 结果为 3.14
        print(f"总共用时：{time_gap}")
        return






if __name__ == "__main__":
    # time_demo()
    # date_time_demo()
    time_counter()

