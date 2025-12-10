#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/10 18:59
# @Author  : mac
# @File    : 05_GroupBy.py
# @Software: PyCharm
'''
按照某个属性分组，左求和或者排序
'''

import pandas as pd

def group_test():
    data = {"Name":["Lily", "Lucy", "Tom", "Li Lei", "Han Meimei"],
            "Department":["HR", "RD", "HR", "Finace","HR"],
            "Salary":[10,222,345,4566,521]}
    df = pd.DataFrame(data)
    print(df)
    #按照部门分组，求他们的平均工资
    group_mean = df.groupby("Department")["Salary"].mean()
    print(group_mean)

def df_data_sort():
    data = {"Name": ["Lily", "Lucy", "Tom", "Li Lei", "Han Meimei"],
            "Department": ["HR", "RD", "HR", "Finace", "HR"],
            "Salary": [1056, 2226, 345, 956, 521]}
    df = pd.DataFrame(data)


    #逆序排序，原始数据没有改变
    df_sort = df.sort_values(by="Salary", ascending=False)
    print(f"sorted ddata = {df_sort}")
    #  打印原始数据
    print(f"original data{df}")


if __name__ == "__main__":
    group_test()
    df_data_sort()