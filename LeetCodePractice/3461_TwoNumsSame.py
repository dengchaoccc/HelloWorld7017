''''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/23 22:38
# @Author  : mac
# @File    : 3461_TwoNumsSame.py
# @Software: PyCharm
3461 判断操作后的字符串是否相等：
给你一个由数字组成的字符串 s 。重复执行以下操作，直到字符串恰好包含 两个 数字：
从第一个数字开始，对于 s 中的每一对连续数字，计算这两个数字的和 模 10。
用计算得到的新数字依次替换 s 的每一个字符，并保持原本的顺序。
如果 s 最后剩下的两个数字 相同 ，返回 true 。否则，返回 false。

示 1：
输入： s = "3902"
输出： true
解释：
一开始，s = "3902"
第一次操作：
(s[0] + s[1]) % 10 = (3 + 9) % 10 = 2
(s[1] + s[2]) % 10 = (9 + 0) % 10 = 9
(s[2] + s[3]) % 10 = (0 + 2) % 10 = 2
s 变为 "292"
第二次操作：
(s[0] + s[1]) % 10 = (2 + 9) % 10 = 1
(s[1] + s[2]) % 10 = (9 + 2) % 10 = 1
s 变为 "11"
由于 "11" 中的数字相同，输出为 true
'''

'''
Python知识点：
1， 怎么把字符串转换为数字
'''


def hasSameDigits(s: str) -> bool:
    temp_str = s
    origin_len = len(temp_str)

    # 负数和长度不够的，都不算
    if (origin_len < 3):
        return False
    if (temp_str[0] == '-'):
        return False

    #输入保证字符串长度从>=3,而且最后肯定是对比2个数，到了剩下2个数就停止循环
    while len(temp_str) > 2:
        sub_str = ""
        for i in range(0, len(temp_str) - 1):
            #题目要求的做法，轮流的求和，再%10，把每个结果记录下来，while循环每一轮都会少一位
            temp_num = (int(temp_str[i]) + int(temp_str[i + 1])) % 10
            sub_str += str(temp_num)
        temp_str = sub_str

    if temp_str[0] == temp_str[1]:
        return True
    else:
        return False


def test_has_same_digit():
    s = "1234324"
    result = hasSameDigits(s)
    print(f"s={s}, is the same={result}")

    s = "1120"
    result = hasSameDigits(s)
    print(f"s={s}, is the same={result}")

    s = "3902"
    result = hasSameDigits(s)
    print(f"s={s}, is the same={result}")


test_has_same_digit()
