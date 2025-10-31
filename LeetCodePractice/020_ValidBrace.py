#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/28 15:54
# @Author  : mac
# @File    : 020_ValidBrace.py
# @Software: PyCharm
'''
20:有效的括号
给定一个只包括（）「」【】的字符串s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
示例1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true
'''

'''
python 知识点：
使用list来模拟栈，主要涉及的操作
1，append 入栈
2，pop出栈
3，len（）判断是否为空
4，a[-1] 获取栈顶元素
'''
class Solution:
    def isValid(self, s: str) -> bool:
        brace_map = {'(': ')', '[': ']', '{': '}'}
        brace_stack = []

        for i in range(0, len(s)):
            if len(brace_stack) == 0:
                brace_stack.append(s[i])
            else:
                temp_char = brace_stack[-1]
                #表示括号已经匹配上了，顶部出栈
                if brace_map.get(temp_char, '') == s[i]:
                    brace_stack.pop()

                else:
                    brace_stack.append(s[i])

        if len(brace_stack) == 0:
            return True

        return False

if __name__ == "__main__":
    obj = Solution()
    s = "()"
    result = obj.isValid(s)
    print(f"string = {s},result = {result}")

    s = "()[]{}"
    result = obj.isValid(s)
    print(f"string = {s},result = {result}")

    s = "()[[]{}"
    result = obj.isValid(s)
    print(f"string = {s},result = {result}")

