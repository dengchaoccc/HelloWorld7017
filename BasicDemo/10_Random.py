#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/10 21:11
# @Author  : mac
# @File    : 10_Random.py
# @Software: PyCharm
'''
对于random类的测试,生成随机数
'''
import  random

def random_num():
    a = random.random()
    print(f" no limit random ={a}")
    a = random.randint(0,12)
    print(f"limit to  int random = {a}")

    a = random.randrange(0,3)
    print(f"limit to 0-3 random = {a}")


def random_range():
    nums = [3,45,667,324,89]
    #随机提取3个数
    result = random.sample(nums,3)
    print(f"random get 3 nums result = {result}")

    result = random.sample(range(0,12), 3)
    print(f"random get 3 nums from 0-12 result = {result}")





if __name__ == "__main__":
    # random_num()
    random_range()