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
    students = [("lily", 156,88), ("Jack", 156, 87), ("Tom", 167,88), ("Lee",178, 89), ("Ray", 178,67) ]
    #按照姓名逆序排序
    students.sort(key = lambda  inputList:inputList[0], reverse=True)
    print(f" sort by name :students = {students}")

    #按照身高从小到大排序
    students.sort(key= lambda  inputList:inputList[1])
    print(f" sort by height :students = \n {students}")

    #使用姓名作为关键字排序,用函数做入参调用
    students.sort(key = compare_student_with_name)
    print(f" sort by self define function :students =\n {students}")

    #先按照身高倒序，再按照分数正序,可以设置多个参数， 这里-号只使用于数字，字符串不能使用
    #(-x[1], x[2]) 是一个元组，作为排序的key值传入排序函数
    #只有x[1],x[2]类型相同才可以这么用
    students.sort(key = lambda x:(-x[1], x[2]))
    print(f" sort by -heigh, +score :students = \n{students}")

    if students:
        print("list is not empty")
    else:
        print("list not empty")

#字典，从大到小和从小到大的排序
'''
这个函数非常值得学习：
1，sorted 排序完了会返回一个列表
2，如果key 和value类型不同，不可以放在一个sorted里做入参。如果参数相同，则可以
   key=lambda x: (x[0], -x[1])来用，
3， 在sorted 里面，如果有限按照value ，再按照key 。那么两层调用的时候，先对key 排序，再对value排序
'''
def test_sort_dict():
    # 创建一个包含键值对的字典，这里banana和potato的值都是5，注意最后输出的结果
    my_dict = {'apple': 10, 'banana': 5, 'potato': 5,'orange': 8, 'grape': 12}
    print(f"before sort mydidt= {my_dict}")
    # 使用sorted函数和lambda表达式对字典按值value排序,如果value相同就按照key从大到小
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[0], reverse= True )
    #调用sorted之后，字典就成为列表了，所以不要加items（）为什么要排序2次，因为key和value是不同类型的
    #注意，这里先要按照key 逆序排列以后，再做value排序，因为必要条件和充分条件有优先级
    sorted_dict = sorted(sorted_dict, key=lambda x: x[1] )

    # 输出排序后的结果
    for item in sorted_dict:
        print(item[0], ":", item[1])


if __name__ == "__main__":
    test_sort_dict()
    test_sort_list()
