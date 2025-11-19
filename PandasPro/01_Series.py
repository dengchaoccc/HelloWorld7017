#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/15 11:43
# @Author  : mac
# @File    : 01_Series.py
# @Software: PyCharm
'''
Series 是 Pandas 中的一个核心数据结构，类似于一个一维的数组，具有数据和索引。
Series 可以存储任何数据类型（整数、浮点数、字符串等），并通过标签（索引）来访问元素。
Series 的数据结构是非常有用的，因为它可以处理各种数据类型，同时保持了高效的数据操作能力，
比如可以通过标签来快速访问和操作数据。
Series 特点：
一维数组：Series 中的每个元素都有一个对应的索引值。
索引： 每个数据元素都可以通过标签（索引）来访问，默认情况下索引是从 0 开始的整数，但你也可以自定义索引。
数据类型： Series 可以容纳不同数据类型的元素，包括整数、浮点数、字符串、Python 对象等。
大小不变性：Series 的大小在创建后是不变的，但可以通过某些操作（如 append 或 delete）来改变。
操作：Series 支持各种操作，如数学运算、统计分析、字符串处理等。
缺失数据：Series 可以包含缺失数据，Pandas 使用NaN（Not a Number）来表示缺失或无值。
自动对齐：当对多个 Series 进行运算时，Pandas 会自动根据索引对齐数据，这使得数据处理更加高效。
'''

import pandas as pd

def create_series():
    #可以自定义索引index
    sef_define_index = [7,8,"z","a","x" ]
    series1 = pd.Series([11,22,33,44,55],index=sef_define_index, name="number list")
    print(series1)
    #根据索引获取值,不是从0开始
    print(f"used self define index , index 7 = {series1[7]}" )

    #根据字典来创建series
    name_map = {1:"Lucy", 2:"Lily", 3:"Tomas"}
    series2 = pd.Series(name_map, name=" user name")
    print(f"user dict {name_map} to create series = {series2}")


def get_series_attributions():
    nums = [23,4,56,6,77,8,20]
    series1 = pd.Series(nums,name = "nums")
    print(f"series = {series1}")

    topx = series1.head(3)
    print(f"first topx value = {topx}")

    indexs = series1.index
    types  = series1.dtypes
    len_of_array = series1.shape
    info = series1.describe() #返回 Series 的统计描述（如均值、标准差、最小值等）
    print(f"index = {indexs}\n type = {types} \n len = {len_of_array} \n  describle = {info}")
    #对数据进行排序
    series2 = series1.sort_values()
    print(f"after sort {series1} ,the result is {series2}")

def get_series_operations() :
    series1 = pd.Series([3,4,1,66,7], index=["a", "b", "c", "d","e"])
    slice1 = series1[1:3]
    print(f"series{series1.values} 1:3 value = {slice1}")

    value_b = series1["b"]
    print(f"try to find index [b] ,value is ={value_b}")
    #和字典类似的操作
    for k, v in series1.items():
        print(f"index = {k}, value = {v}")

    #和字典一样的赋值
    series1["f"] = 12
    series1['a'] = 466
    print(f"after insert series{series1}")

    #一些算术运算，其实就是describe 里面的内容
    print(series1.sum())  # 输出 Series 的总和
    print(series1.mean())  # 输出 Series 的平均值
    print(series1.max())  # 输出 Series 的最大值
    print(series1.min())  # 输出 Series 的最小值
    print(series1.std())  # 输出 Series 的标准差





if __name__ == "__main__":
    # create_series()
    #get_series_attributions()
    get_series_operations()