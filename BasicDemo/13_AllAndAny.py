#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/15 11:05
# @Author  : mac
# @File    : 13_AllAndAny.py
# @Software: PyCharm
'''
all 和any的测试
'''

def all_any_demo():
    nums = [34,1,545,43,23,112]

    result = all(x > 100 for x in nums)
    print(f"nums = {nums},all x>100 result is {result} ")
    #any只要有一次满足就可以返回True
    result = all(nums)
    print(f"nums = {nums},all nums is {result} ")

    #判断集合是否非空
    result = any(x > 100 for x in nums)
    print(f"nums = {nums},all result is {result} ")

if __name__ == "__main__":
    all_any_demo()

