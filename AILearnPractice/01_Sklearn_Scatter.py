#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/9 11:16
# @Author  : mac
# @File    : 01_Sklearn_Scatter.py
# @Software: PyCharm
'''
逻辑回归-散点图的训练
'''
import  pandas as pd
import numpy as np
from sklearn.linear_model import  LogisticRegression
import matplotlib.pyplot as plt

#从csv中读取散点图数据，并且读取标签，然后做预测
'''
逻辑回归函数 P(x) = 1/(1 + e**-x )
            P(x) = 1/(1 + e**-g(x) )
            g(x) = θo+θ₁X₁+θ₂X₂=0 
            如果你要变成曲线，那么就要用平方二阶函数          
'''
def read_data(file_name:str):
    df  = pd.read_csv(file_name)
    x = []
    y = []
    label = []
    rows, columns = df.shape

    for i in range(0, rows):
        x.append(df.iloc[i,0])
        y.append(df.iloc[i, 1])
        label.append(df.iloc[i, 2])
    #画个散点图
    np_x = np.array(x)
    np_y = np.array(y)
    np_label = np.array(label)

    mask = (np_label == True)
    plt.scatter(np_x[mask], np_y[mask],c="red",label = "Passed")
    plt.scatter(np_x[~mask], np_y[~mask],c="blue",label = "Failed")
    plt.title('Random Scatter Plot with Two Classes')
    plt.legend()#没这句话，label不会显示出来
    #plt.show()#没有这句话，散点图不会显示出来
    return x,y,label

def logic_reg():
    x,y,label = read_data("scatter_xy.csv")

    # 使用np.column_stack函数将x和y合并为两列的二维数组
    combined_array = np.column_stack((x, y))

    logic_re = LogisticRegression()
    logic_re.fit(combined_array,label)#训练逻辑回归,得到θo+θ₁X₁+θ₂X₂=0
    print(logic_re.coef_)#x有2个特征，就有2个系数θ₁和θ2
    print(logic_re.intercept_)#这个是θ0，截距，也就是常数
    print(f"回归后的方程:{logic_re.intercept_[0]:3f} + {logic_re.coef_[0][0]:3f}*x1 + {logic_re.coef_[0][1]:3f}*x2 = 0")

    prediction = logic_re.predict([[12,34],[54,13]]) #这个值应该是True，false
    print(f"输入两个点的预测结果：{prediction}")


if __name__ == "__main__":
    logic_reg()