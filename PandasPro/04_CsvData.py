#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/22 11:22
# @Author  : mac
# @File    : 04_CsvData.py
# @Software: PyCharm

import  pandas as pd

def read_cvs_as_df():
    pf1 = pd.read_csv("nba.csv",sep=";")
    print(f"{pf1.head(2)}")
    pf1.to_csv("nba_copy.csv")#保存备份一下

    rows,cloumns = pf1.shape
    print(f"rows = {rows}, series number = {cloumns}")

    for i in range(2):
        for j in range(cloumns):
            print(f"i = {i}, j = {j}, content = {pf1.iloc[i,j]}")



if __name__ == "__main__":
    read_cvs_as_df()
