#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/27 10:31
# @Author  : mac
# @File    : 393_SubstringDelet.py
# @Software: PyCharm
'''
392:判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false
'''

'''
python 知识点：
在 Python 中：for i in range(0, 5) 循环结束后，i 的值是 4。
在 C/Java 等语言中：for (int i=0; i<5; i++) 循环结束后，i 的值是 5。
Python 的 for-in 循环机制与这种传统的 for 循环不同，它是迭代器模式，逐个从序列中取出值，取完即止
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        origin_index = 0
        find_flag = False

        for i in range(0, len(s)):

            find_flag = False
            for j in range(origin_index, len(t)):

                if (s[i] == t[j]):
                    origin_index = j + 1
                    find_flag = True
                    break
            if not find_flag:
                return False

        return True

if __name__ == "__main__":
    obj = Solution()
    s = "abc"
    t = "ahbgdc"
    result = obj.isSubsequence(s,t)
    print(f"s={s},t={t},result ={result}")

    s = "axc"
    t = "ahbgdc"
    result = obj.isSubsequence(s, t)
    print(f"s={s},t={t},result ={result}")