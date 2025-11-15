#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/13 11:39
# @Author  : mac
# @File    : 12_GussNumber.py
# @Software: PyCharm
import  random
from datetime import datetime
def generate_random():
    num = random.randrange(0,99)
    return num

def number_game():

    guss_input = input("请猜一个数，数字在0-99之间，现在开始输入数字：")
    start_time = datetime.now()
    num = generate_random()

    while True:
        if not guss_input.isdigit() :
            guss_input = input("输入的数字不合法，请再次输入")
            continue
        guss_input = int(guss_input)
        if guss_input > num:
            guss_input = input(f"数字{guss_input}太大了，请再次输入")
        elif guss_input < num:
            guss_input = input(f"数字{guss_input}太小了，请再次输入")
        else:
            end_time = datetime.now()
            time_cost = end_time- start_time
            print(f"恭喜你猜对了，数字是{num},用时{time_cost}秒")
            return

if __name__ == "__main__":
    number_game()