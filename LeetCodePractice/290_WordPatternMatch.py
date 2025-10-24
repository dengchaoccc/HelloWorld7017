#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/23 22:23
# @Author  : mac
# @File    : 290_WordPatternMatch.py
# @Software: PyCharm
'''
给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。具体来说：
pattern 中的每个字母都 恰好 映射到 s 中的一个唯一单词。
s 中的每个唯一单词都 恰好 映射到 pattern 中的一个字母。
没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。

示例1:
输入: pattern = "abba", s = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", s = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false
'''

'''
Python知识点：
1，怎么通过取下标获取字符串的字符
2，怎么通过空格把字符串分割成单词
3，怎么在字典里获取所有的值和key
'''
def wordPattern(pattern: str, s: str) -> bool:
    # 字符串根据空格拆开
    words = s.split()
    patter_len = len(pattern)
    word_number = len(words)

    pattern_word_map = {}

    if (patter_len != word_number):
        return False

    for i in range(0, patter_len):

        """
        #第一个条件，如果它们没有凑对，就给凑对,比如 abab  do,ca,do ca
        #第二个条件，如果凑对过，也要检查是否value.比如aba  do,do,do
        """
        if pattern_word_map.get(pattern[i], "") == "" and \
                words[i] not in pattern_word_map.values():
            pattern_word_map[pattern[i]] = words[i]
            continue
        if pattern_word_map.get(pattern[i], "") != words[i]:
            return False

    return True

def test_string_pattern_match():
    pattern = "abba"
    s = "dog cat cat fish"
    result = wordPattern(pattern,s)
    print(f"pattern ={pattern},word={s}, result ={result}")

    pattern = "abbc"
    s = "dog cat cat fish"
    result = wordPattern(pattern, s)
    print(f"pattern ={pattern},word={s}, result ={result}")

    pattern = "aac"
    s = "dog dog dog"
    result = wordPattern(pattern, s)
    print(f"pattern ={pattern},word={s}, result ={result}")

    pattern = "aa"
    s = "dog dog dog"
    result = wordPattern(pattern, s)
    print(f"pattern ={pattern},word={s}, result ={result}")

test_string_pattern_match()