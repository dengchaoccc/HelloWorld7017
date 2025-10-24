#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/24 15:24
# @Author  : mac
# @File    : 058_LenOfLastWord.py
# @Software: PyCharm
'''
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
提示：
1 <= s.length <= 104
s 仅有英文字母和空格 ' ' 组成
s 中至少存在一个单词

示例 1：
输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为 5。
'''
'''
pyton新知识：
1，怎么在类里面使用__main__函数
2，range从后往前遍历
3，字符里判断是否字母，数字等，都是有内置函数的
'''
class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        '''
        方法1：直接调用库函数，2行搞定
        words = s.split()
        return len(words[-1])
        '''
        #方法2：从后往前遍历, range三个参数表示：起始，终止，步长
        word_len = 0
        for i in range(len(s)-1, -1, -1):
            if s[i].isalpha():
                word_len += 1
            elif s[i] == ' ': #这里是为了防止最后一个全是空格
                if word_len == 0:
                    continue
                else:#走道这里，一个单词就抠出来了
                    break
            else:
                continue
        return word_len

if __name__ == "__main__":
    obj = Solution()
    s = "   fly me   to   the moon   "
    len1 = obj.lengthOfLastWord(s)
    print(f"s = {s}, last word len ={len1}")

    s = "  hello   world "
    len1 = obj.lengthOfLastWord(s)
    print(f"s = {s}, last word len ={len1}")

    s = ' '
    print(f"s = {s}, isalpha ={s.isalpha()}")
    s = ''
    print(f"s = {s}, isalpha ={s.isalpha()}")
    s = 'x'
    print(f"s = {s}, isalpha ={s.isalpha()}")
    s = '&'
    print(f"s = {s}, isalpha ={s.isalpha()}")