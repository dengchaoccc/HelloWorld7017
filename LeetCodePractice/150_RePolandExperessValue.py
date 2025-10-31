#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/31 10:50
# @Author  : mac
# @File    : 150_RePolandExperessValue.py
# @Software: PyCharm
'''
给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

注意：

有效的算符为 '+'、'-'、'*' 和 '/' 。
每个操作数（运算对象）都可以是一个整数或者另一个表达式。
两个整数之间的除法总是 向零截断 。
表达式中不含除零运算。
输入是一个根据逆波兰表示法表示的算术表达式。
答案及所有中间计算结果可以用 32 位 整数表示。


示例 1：
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：
输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
示例 3：
输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

'''


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        oprations = ["+", "-", "*", "/"]
        stack = []

        for temp in tokens:
            # 这种情况，必定是数字
            if temp not in oprations:
                num = int(temp)
                stack.append(num)
            else:
                # 遇到了操作符，说明栈里至少有2个数字，把2个数字操作
                if len(stack) < 2:
                    print(f"len too small,temp={temp},stack={stack}")
                    continue
                num1 = stack.pop()
                num2 = stack.pop()
                total = 0
                if temp == "+":
                    total = num1 + num2
                elif temp == "-":
                    total = num2 - num1
                elif temp == "*":
                    total = num1 * num2
                elif temp == "/":
                    total = int(num2 / num1)
                else:  # 纯粹为了保持分支完整才加的这句话
                    print(f"uepected string{temp}")

                # 临时结果保存，用来和下一个数字进行计算
                stack.append(total)

        return stack[0]

if __name__ == "__main__":
    obj = Solution()
    tokens = ["2","1","+","3","*"]
    result = obj.evalRPN(tokens)
    print(f"str = {tokens}, result = {result}")

    tokens = ["4","13","5","/","+"]
    result = obj.evalRPN(tokens)
    print(f"str = {tokens}, result = {result}")

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = obj.evalRPN(tokens)
    print(f"str = {tokens}, result = {result}")

    tokens = ["10"]
    result = obj.evalRPN(tokens)
    print(f"str = {tokens}, result = {result}")