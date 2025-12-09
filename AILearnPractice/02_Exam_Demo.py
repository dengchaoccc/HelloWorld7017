#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/9 17:24
# @Author  : mac
# @File    : 02_Exam_Demo.py
# @Software: PyCharm
'''
逻辑回归案例：
根据学生的2门课程的成绩，给出第三门成绩的结果。
给出一个学生前面2门考试的成绩，预测他是否可以通过第三门考试
'''

import  pandas as pd
import numpy as np
from sklearn.linear_model import  LogisticRegression
import  matplotlib.pyplot as plt

#从excel里读取数据，要求数据行数必须要一致
def parse_data(file_name):
    exam1 = []
    exam2 = []
    passed = []
    df = pd.read_csv(file_name)

    rows, columns = df.shape

    for i in range(0, rows):
        exam1.append(df.iloc[i,0])
        exam2.append(df.iloc[i, 1])
        passed.append(df.iloc[i, 2])
    return exam1, exam2, passed

def logic_reg():
    exam1, exam2,passed = parse_data("exam.csv")

    #两个特征列合并
    x = np.column_stack((exam1,exam2))
    y = passed
    logic_re = LogisticRegression()
    #fit的第一个参数必须是二维的，第二个参数是1维的

    logic_re.fit(x, y)

    X1 = np.array(exam1)
    theta0 = logic_re.intercept_[0]
    theta1 = logic_re.coef_[0][0]
    theta2 = logic_re.coef_[0][1]
    #θo + θ₁X₁+θ₂X₂=0
    X2 = -(theta0 + theta1*X1)/theta2


    #散点图打印
    np_label = np.array(passed)
    mark = (np_label == 1)
    exam1_np = np.array(exam1)
    exam2_np = np.array(exam2)
    plt.scatter(exam1_np[mark], exam2_np[mark],c="red",label = "Exam1")
    plt.scatter(exam1_np[~mark], exam2_np[~mark], c="blue", label = "Exam2")
    plt.plot(X1,X2)#打印决策边界
    plt.legend()#显示标签
    plt.show()

    #预测这个学生能否通过考试
    prediction = logic_re.predict([[75,54]])
    print(prediction[0])



if __name__ == "__main__":
    logic_reg()

