#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/27 14:37
# @Author  : mac
# @File    : 013_RomanToNumber.py
# @Software: PyCharm
'''
13:罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
        sum = 0
        len1 = len(s)

        for i in range(0, len1):
            #遇到4,9,40等情况，左边的数比右边的小，那么就是扣除，用负数替代
            if i < len1 -1 and num_dict[s[i]] < num_dict[s[i+1]]:
                sum -= num_dict[s[i]]
            else:
                sum += num_dict[s[i]]
        return sum

if __name__ == "__main__":
    obj = Solution()
    s = "LVIII"
    num = obj.romanToInt(s)
    print(f"s={s}, value = {num}")

    s = "MCMXCIV"
    num = obj.romanToInt(s)
    print(f"s={s}, value = {num}")

    s = "MMMXCIV"
    num = obj.romanToInt(s)
    print(f"s={s}, value = {num}")