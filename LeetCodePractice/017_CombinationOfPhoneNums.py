#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/30 14:26
# @Author  : mac
# @File    : 017_CombinationOfPhoneNums.py
# @Software: PyCharm
'''
017:电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如诺基亚按键手机，比如2 对应abc（与电话按键相同）。注意 1 不对应任何字母。
示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：
输入：digits = "2"
输出：["a","b","c"]

1 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

例如：digits = 235
2    3   5
abc def jkl
队列：a-ad-adj-ad-adk-ad-adl-ad-a-ae-aej-ae-aek-ae-ael-ae-a-af-afj-af-afk-af-afl-af-a-[]-b-bd-
bdj-bd-...
'''

'''
python 知识点：
1，str类型是没有append和pop的概念的，只能通过+ 和切片来做到添加成员和删除成员
2，回溯法，递归调用的5个步骤是一个经典算法，必须要学会的
3，字典dict 最好是使用get ，而不是dic[key]，get可以写一个默认值，允许出错
'''

class Solution:

    def dfs(self, alpha_index, alpha_collection, temp_str, result):

        # 1，递归终止条件：如果最后一个凑成了字符了，要保存起来。一定要有终止，否则就是死循环
        if alpha_index >= len(alpha_collection):
            result.append("".join(temp_str))
            return

        # 2，本层递归开始，挨个遍历本层的成员，
        alphas = alpha_collection[alpha_index]
        for char1 in alphas:
            # 3,找到一个成员，新成员入栈
            temp_str = temp_str + str(char1)
            # 4,递归调用，填写下一个字母
            self.dfs(alpha_index + 1, alpha_collection, temp_str, result)
            # 5,递归后本成员弹出,把最后一个字符删除。这样本层的下一个成员又可以继续执行操作
            temp_str = temp_str[:-1]

    def letterCombinations(self, digits: str) -> list[str]:
        number_map = {"2": "abc",
                      "3": "def", "4": "ghi", "5": "jkl",
                      "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        alpha_collection = []

        # 数字全部转化为字符
        for i in digits:
            result = []
            alphas = number_map.get(i, "")
            alpha_collection.append(alphas)

        # 深度优先递归调用
        result = []
        temp_str = ""
        self.dfs(0, alpha_collection, temp_str, result)

        return result

if __name__ == "__main__":
    obj = Solution()
    digits = "23"
    result = obj.letterCombinations(digits)
    print(f"digits={digits}, combination = {result}")

    digits = "2"
    result = obj.letterCombinations(digits)
    print(f"digits={digits}, combination = {result}")

    digits = "249"
    result = obj.letterCombinations(digits)
    print(f"digits={digits}, combination = {result}")

