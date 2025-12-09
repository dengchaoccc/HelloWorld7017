#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/5 17:54
# @Author  : mac
# @File    : 00_Sklearn_Linear.py
# @Software: PyCharm
# 线性回归的一个举例,从一堆的x，y的散列点中，找到拟合类似的线性曲线#

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

'''
从csv里读取x和y的散列点信息
'''
def read_data(file_name):
    x_array = []
    y_array = []

    df = pd.read_csv(file_name)

    # 画一个散点图
    df.plot(kind='scatter', x='x', y='y')
    # 画一个折线图
    #df.plot(kind='line')
    #plt.show()#一定要show才可以显示画图结果

    rows= df.shape[0]

    for i in range(0,rows):

        # print(f"i = {df.iloc[i,0]}, {df.iloc[i,1]} ")
        x_array.append(int(df.iloc[i,0]))
        y_array.append(int(df.iloc[i,1]))

    return x_array, y_array

'''
最小二乘法做线性回归
'''
def sk_learn_demo():
    reg = linear_model.LinearRegression()
    x_array, y_array = read_data("Linear_xy.csv")
    '''
    X{array-like, 稀疏矩阵}，形状为 (n_samples, n_features)训练数据。有m行数据，每一行有n个特征（n列）
    y array-like，形状为 (n_samples,) 或 (n_samples, n_targets)目标值。如果需要，将转换为 X 的 dtype。
    它表示每个样本的目标（即输出标签），通常是一个一维数组
    '''

    #我自己的预测，是y = 2x + 5：斜率=2，截距=5
    #从一维数组转换为二维数组，并且规定-1自动计算行数， 每行固定1列
    x = np.array(x_array).reshape(-1,1)
    y = np.array(y_array).reshape(-1,1)
    reg.fit(x, y)
    #我的预测是2x+5
    print(f" f(x ）= {reg.coef_[0][0]:.2f}x + {reg.intercept_[0]:.2f} ")

    expect_val = reg.predict([[13]])
    print(expect_val)



''''
第二个例子，使用随机数生成输入的数据
'''
def self_training():
    '''
    在机器学习/科学计算中：你的模型训练可能依赖于随机初始化参数、随机打乱数据或随机丢弃神经元。
    如果不固定种子，每次运行结果都不同，你将无法判断模型效果的提升是源于代码改进，还是运气
    相同的种子一定会产生完全相同的“随机”序列
    :return:
    '''
    np.random.seed(42)
    n_samples = 100
    #reshape  -1 表示自动计算， 1表示1列。 那么就是N行1列
    x = np.linspace(0, 10, n_samples).reshape(-1, 1)  # 生成0到10的100个点,等间距数组，把一维度、转换为二维

    #人工监督，我自己的的预测试2x+5
    true_slope = 2.0  # 真实斜率
    true_intercept = 5.0  # 真实截距
    noise = np.random.randn(n_samples, 1) * 1.5  # 加点噪声，数据看起来更加真实，扩大1.5倍
    y = true_slope * x + true_intercept + noise

    #训练模型
    reg = linear_model.LinearRegression()
    print(f"x形状: {x.shape}")  # (100, 1)
    print(f"y形状: {y.shape}")  # (100, 1)
    reg.fit(x,y)

    print("\n=== 模型结果 ===")
    print(f"真实函数: y = {true_slope}x + {true_intercept}")
    print(f"学到的系数 (coef_): {reg.coef_[0][0]:.4f}")
    print(f"学到的截距 (intercept_): {reg.intercept_[0]:.4f}")
    print(f"学到的函数: y = {reg.coef_[0][0]:.4f}x + {reg.intercept_[0]:.4f}")

    # 3. 使用模型预测
    x_test = np.array([[2.5], [5.0], [7.5]])  # 2.5, 5.0, 7.5 是你想要预测的新的X值（输入特征值）
    y_pred = reg.predict(x_test)

    print("\n=== 预测示例 ===")
    for i in range(len(x_test)):
        true_y = true_slope * x_test[i][0] + true_intercept
        print(f"x={x_test[i][0]}: 预测={y_pred[i][0]:.4f}, 真实={true_y:.4f}")




if __name__ == "__main__":
    sk_learn_demo()
    #self_training()
