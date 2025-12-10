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
from sklearn.metrics import accuracy_score
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

def basic_logic_reg():
    exam1, exam2,passed = parse_data("exam.csv")

    #两个特征列合并
    x = np.column_stack((exam1,exam2))
    y = passed
    logic_re = LogisticRegression(max_iter=100)
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

#使用二次方程来模拟决策曲线
def advanced_logic_regression():
    exam1, exam2, passed = parse_data("exam.csv")
    # 回归函数：θ0+θ1X1+θ2X:+θ3*X1平方+θ4*X2平方+θ5X1X2=0
    X1 = np.array(exam1)
    X2 = np.array(exam2)
    #创建新数据，用户做回归曲线
    X1_X1 = X1 * X1
    X2_X2 = X2 * X2
    X1_X2 = X1 * X2
    y = np.array(passed)
    x = np.column_stack((X1,X2,X1_X1,X2_X2,X1_X2))
    #m默认100次迭代没办法收敛，这里把迭代次数设置大一些
    logic_reg2 = LogisticRegression(max_iter=1000)
    logic_reg2.fit(x,y)

    #为预测的准确率打分，左评估
    y2_predict = logic_reg2.predict(x)

    accurcy1 = accuracy_score(y, y2_predict) #注意，这还有个模块叫做accuracy_scorer，别用混淆了

    #开始画图，看看有几个因子，应该有4个
    print(len(logic_reg2.coef_))
    theta0 = logic_reg2.intercept_
    theta1 = logic_reg2.coef_[0][0]
    theta2 = logic_reg2.coef_[0][1]
    theta3 = logic_reg2.coef_[0][2]
    theta4 = logic_reg2.coef_[0][3]
    theta5 = logic_reg2.coef_[0][4]

    #此处排序是为了避免画图的时候，线条交错杂乱
    X1 = np.sort(X1)

    # θ0 + θ1X1 + θ2X: +θ3 * X1平方 + θ4 * X2平方 + θ5X1X2 = 0
    a = theta4
    b = theta5*X1 + theta2
    c = theta0 + theta1*X1 + theta3*X1*X1


    #这个就是二次方程的求解，有2个根，我们只要正数根 a*x平方+ bx + c = 0，那么求函数的根
    X2_boudary = (-b + np.sqrt( np.abs(b*b - 4*a*c)))/(2*a)
    figure1 = plt.figure()
    #打印边界二阶决策
    plt.plot(X1, X2_boudary)

    # 散点图打印
    np_label = np.array(passed)
    mark = (np_label == 1)
    exam1_np = np.array(exam1)
    exam2_np = np.array(exam2)
    plt.scatter(exam1_np[mark], exam2_np[mark], c="red", label="Exam1")
    plt.scatter(exam1_np[~mark], exam2_np[~mark], c="blue", label="Exam2")

    plt.show()





if __name__ == "__main__":
    #basic_logic_reg
    advanced_logic_regression()




