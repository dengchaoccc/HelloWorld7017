#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/12 11:23
# @Author  : mac
# @File    : 08_Input.py
# @Software: PyCharm
'''
输入的测试
'''

def input_sort():
    nums = []
    for i in range(0,3):
        try:
            a = input("输入一个整数")
            if a.isdigit():
                a = int(a)
                nums.append(a)
        finally:
            print(f"input index = {i}")
    print(f"before sort a = {nums}")
    nums.sort()
    print(f"after sort nums = {nums}")

if __name__ == "__main__":
    input_sort()
