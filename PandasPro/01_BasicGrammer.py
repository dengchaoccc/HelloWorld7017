#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/15 11:20
# @Author  : mac
# @File    : 01_BasicGrammer.py
# @Software: PyCharm
'''
前提是安装了pandas资源包
python3 -m pip install pandas 安装
Pandas 是一个开源的数据分析和数据处理库，它是基于 Python 编程语言的。
Pandas 提供了易于使用的数据结构和数据分析工具，特别适用于处理结构化数据，如表格型数据（类似于Excel表格）。
Pandas 是数据科学和分析领域中常用的工具之一，它使得用户能够轻松地从各种数据源中导入数据，并对数据进行高效的操作和分析。
Pandas 主要引入了两种新的数据结构：Series 和 DataFrame。
Series： 类似于一维数组或列表，是由一组数据以及与之相关的数据标签（索引）构成。
Series 可以看作是 DataFrame 中的一列，也可以是单独存在的一维数据结构。

DataFrame： 类似于一个二维表格，它是 Pandas 中最重要的数据结构。
DataFrame 可以看作是由多个 Series 按列排列构成的表格，
它既有行索引也有列索引，因此可以方便地进行行列选择、过滤、合并等操作。
DataFrame 由 Index、Key、Value 组成：
'''

import pandas as pd

def merge_series():
    apple_series = pd.Series([1,3,4,5,332,2,7])
    banana_series = pd.Series([11,23,45,26,76,44])

    # 将两个Series对象相加，得到DataFrame，并指定列名
    data_frame = pd.DataFrame({"Apple": apple_series, "Banana": banana_series})
    print(data_frame)

if __name__ == "__main__":
    merge_series()
