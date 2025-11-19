#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/15 15:27
# @Author  : mac
# @File    : 02_DataFrame.py
# @Software: PyCharm
'''
DataFrame 是 Pandas 中的另一个核心数据结构，类似于一个二维的表格或数据库中的数据表。
DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。
DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。
DataFrame 提供了各种功能来进行数据访问、筛选、分割、合并、重塑、聚合以及转换等操作。
DataFrame 是一个非常灵活且强大的数据结构，广泛用于数据分析、清洗、转换、可视化等任务。

DataFrame 构造方法如下：
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
参数说明：
data：DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame。
index：DataFrame 的行索引，用于标识每行数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
'''

import pandas as pd

def create_data_frame():
    #用列表创建数据
    students_map = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
    clomn_name = ["name", "age"]
    df1 = pd.DataFrame(students_map, columns= clomn_name)
    #可以自己设置类型
    df1["name"] = df1["name"].astype(str)
    print(df1)
    #也可以用字典创建，这样就不需要clomns_name了
    data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

    df2 = pd.DataFrame(data)
    print(df2)
    #获取一行内容，可以使用at或者loc ，at更加高效
    print(f"df1[0]=\n{df1.loc[0]}, df[1]= \n{df1.loc[1]}")

    #一共2行，每列都有一个标题头
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    #index是每一行的索引
    df3 = pd.DataFrame(data, index=["day1", "day2", "day3"])
    print(f"df3 = {df3}")

    # 通过字典创建 DataFrame
    df4 = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
    df5 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                      columns=['Column1', 'Column2', 'Column3'])
    # 从 Series 创建 DataFrame
    s11 = pd.Series(['Alice', 'Bob', 'Charlie'])
    s22 = pd.Series([25, 30, 35])
    s33 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
    df6= pd.DataFrame({'Name': s11, 'Age': s22, 'City': s33})
    #添加新列
    df6['NewAddColumn'] = [100, 200, 300]

    # 使用 loc 为特定索引添加新行，如果值存在就改写，如果不存在就新增
    df6.loc[4] = ["Toma","22", "Boston1", 15]
    #非常不推荐使用apend，麻烦很多，必须要用字典，而且要有返回值
    new_row = {"Name":"Mark", "Age":18,"City":"Houseton", "NewAddColumn":324}
    #主要原因是在使用 _append 方法时，它默认不会修改原始DataFrame，而是返回一个包含新增数据的新DataFrame对象
    df6= df6._append(new_row, ignore_index=True)
    #并不会插入到第九行，而是在后面追加，实际插入第七行
    df6.loc[9] = ["Alex", "24", "DC", 345]
    df6.to_csv("create_dataframe_demo.csv", index=False)


def user_info_data_frame():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    df1 = pd.DataFrame(data)

    #查看前几行数据
    print(f"look head 2 lines : = {df1.head((2))}")
    #查看基本信息
    print(f"look basic info = {df1.info}")
    #查看统计信息
    print(f"describle = {df1.describe()}")

    #查看指定列,名字一定要写对，要不然不行
    clomn_names = df1.columns
    print(f"just look age and name = {df1[clomn_names[:2]]}")
    #选择切片，1到2行
    print(f"slice line 1:3 = {df1.iloc[1:3]}")
    # 计算分组统计（按城市分组，计算平均年龄）
    print(df1.groupby('City')['Age'].mean())

    df1.to_csv('output_Data_frame_test.csv', index=False)

def create_by_series():
    s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
    s2 = pd.Series([25, 30, 35])
    s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
    df = pd.DataFrame({'Name': s1, 'Age': s2, 'City': s3})
    print(df)
    return df

#简单的行列遍历
def data_frame_visit():
    df = create_by_series()


    row1 = df.iloc[1]
    print(f"1st row = {row1}")
    row1 = df.iloc[0:2]
    print(f"1 and 2 row = {row1}")
    row1 = df.iloc[2,0]#严格的数字，2行0列
    print(f"1 row , 1st column= {row1}")
    row1 = df.loc[2, "Name"] #2行 名字列，如果iloc必须是全部数字，这里第二个可以是字符串
    print(f"1 row , 1st column= {row1}")

    rows, cols = df.shape
    for i in range(0,rows):
        for j in range(0,cols):
            print(df.iloc[i,j])





if __name__ == "__main__":
    create_data_frame()
    user_info_data_frame()
    data_frame_visit()
