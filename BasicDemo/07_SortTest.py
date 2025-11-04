#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/4 10:52
# @Author  : mac
# @File    : 07_SortTest.py
# @Software: PyCharm
# 一些关于排序的测试



'''
假设姓名存在数组的第一个位置，直接用第一个元素
'''
def compare_student_with_name(single_student):
    return single_student[0]

'''
list. sort 会自动进行排序
backup = sorted(list) 会建立一个副本，本体不做变更
'''
def test_sort_list():
    '''
    用[]是列表，数组，长度可变，元素可以是不同类型的
    用（）包围的是元组，里面的数据可以是不同的类型，长度不可变
    '''
    students = [("lily", 156,88), ("Jack", 156, 88), ("Tom", 167,8872), ("Lee",132, 89), ("Ray", 178,67) ]
    #按照姓名逆序排序
    students.sort(key = lambda  inputList:inputList[0], reverse=True)
    print(students)

    #按照身高从小到大排序
    students.sort(key= lambda  inputList:inputList[1])
    print(students)

    #使用姓名作为关键字排序,用函数做入参调用
    students.sort(key = compare_student_with_name)
    print(students)

    #先按照身高倒序，再按照分数正序,可以设置多个参数
    students.sort(key = lambda x:(-x[1], x[2]))
    print(students)

    if students:
        print("list is not empty")
    else:
        print("list not empty")


