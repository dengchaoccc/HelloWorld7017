#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/5 22:50
# @Author  : mac
# @File    : 09_FunctionCallTest.py
# @Software: PyCharm
'''
对于函数调用的一些测试，主要测试入参是否会改变
'''

#传入的简单类型的值，不会被改变
def change_value(a,b): # 此时a指向5，b指向6
    a = a +1  # 创建新对象6，局部变量a现在指向6
    b = b - 1 # 创建新对象5，局部变量b现在指向5
    # 函数结束，局部变量a,b被销毁

def test_change_value():
    a = 5
    b = 6
    change_value(a,b)
    print(f"after change value a = {a},b= {b}")

#复杂类型的参数，传入进来是可以改变对象的内容的
def change_by_list(l, value):
    l.append(value)

#尝试把一个临时变量赋值给入参,发现函数完了以后，l还是原来的值
def change_list_obj(l):
    l1 = [0]*5
    l = l1
    print(f"inside func ,l = {l}")

def test_change_by_list():
    l = [2,3,4,5,6]
    change_by_list(l,7)
    change_by_list(l,8)
    print(f"after change value l = {l}")

    change_list_obj(l)
    print(f"after change list value l = {l}")

if __name__ == "__main__":
    test_change_value()
    test_change_by_list()

