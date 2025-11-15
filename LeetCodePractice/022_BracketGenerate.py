#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/6 10:33
# @Author  : mac
# @File    : 022_BracketGenerate.py
# @Software: PyCharm
'''
022:括号生成， 中级
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
输入：n = 1
输出：["()"]
'''

'''
python 知识点：
1，深度优先的递归调用几个步骤
2，list.append ，如果元素是一个对象，就要添加对象的副本，而不是原来的对象，原来的对象会变
3，排列组合的问题，通用套路只有这一个，无非就是多一些剪枝处理
'''
class Solution:
    def dfs(self, current_list, answer, left, right, n):
        # 队列已满，必须返回
        if len(current_list) == 2 * n:
            if left == right:
                # 注意此处不要用answer.append((current_list))，否则字符串会同步改动
                # 这里要保存的是副本，而不是字符串对象
                answer.append("".join(current_list))
            return

        # 剪枝处理
        if left > n or right > n:
            return

        if left < n:
            current_list = current_list + "("
            self.dfs(current_list, answer, left + 1, right, n)
            current_list = current_list[:-1]

        if right < left:
            current_list = current_list + ')'
            self.dfs(current_list, answer, left, right + 1, n)
            current_list = current_list[:-1]

        return

    def generateParenthesis(self, n: int) -> list[str]:
        answer = []
        current_list = ""

        self.dfs(current_list, answer, 0, 0, n)

        return answer


if __name__ == "__main__":
    obj = Solution()
    n = 1
    result = obj.generateParenthesis(n)
    print(f"n = {n}, result = {result}")

    n = 3
    result = obj.generateParenthesis(n)
    print(f"n = {n}, result = {result}")

    n = 4
    result = obj.generateParenthesis(n)
    print(f"n = {n}, result = {result}")