#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/8 14:09
# @Author  : mac
# @File    : 15_ClassInheritance.py
# @Software: PyCharm
'''
作为面向对象，类的编写和实验
'''

class Person():
    name = ""
    age = 0
    _weight = 0 #下划线开头的都是私有变量，但是python不会禁止你访问它，全靠自觉
    def __init__(self, name:str,  age:int,  weight:int):
        self.name = name
        self.age = age
        self._weight = weight
    def speak(self):
        print("我是一个Person")

#单继承，如果有多个父类，可以在括号里写
class Chinse(Person):
    user_id:int

    #重写构造方法
    def __init__(self, name: str, age: int, weight: int, user_id:int):
        #直接调用父类构造函数,这里self也要传入
        Person.__init__(self,name,age,weight)
        self.user_id = user_id
    def speak(self):
        # 覆写父类的方法
        print(f"id = {self.user_id}, name = {self.name}, age={self.age:4d}")

if __name__  == "__main__":
    chn = Chinse("Li Hua", 12, 40, 2223)
    chn.speak()




