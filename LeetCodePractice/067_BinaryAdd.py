#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/29 18:08
# @Author  : mac
# @File    : 067_BinaryAdd.py
# @Software: PyCharm
'''
67，二进制相加
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

示例 1：
输入:a = "11", b = "1"
输出："100"
示例 2：
输入：a = "1010", b = "1011"
输出："10101"
提示：
1 <= a.length, b.length <= 104
a 和 b 仅由字符 '0' 或 '1' 组成
字符串如果不是 "0" ，就不含前导零
'''

'''
思路就是把位数用0补齐，然后逐个相加，注意进位即可
python知识点：
1，怎么初始化全是一样元素的字符串或者数组
2，字符串拼接的时候，主要先后顺序
'''
class Solution:

    def addBinary(self, a: str, b: str) -> str:
        len1 = len(a)
        len2 = len(b)

        # 先把短的字符串位数用0补齐
        gap = abs(len1 - len2)
        temp_str = "0" * gap

        if len1 > len2:
            str1 = a
            str2 = temp_str + b
        else:
            str1 = b
            str2 = temp_str + a

        extra_add = 0
        ans_str = ""

        for i in range(len(str1) - 1, -1, -1):
            # 求和结果就只有0,1,2三种可能
            sum = int(str1[i]) + int(str2[i]) + extra_add
            if (sum > 1):
                extra_add = 1
            else:
                extra_add = 0
            # 只获取最末尾的1位数
            sum = sum & 1
            # 注意顺序，新加的数要放在最左边
            ans_str = "".join(str(sum)) + ans_str

        # 最末尾，如果有个1，要额外加到最左边
        if extra_add:
            ans_str = "1" + ans_str

        return ans_str


if __name__ == "__main__":
    obj = Solution()
    a = "11"
    b = "1"
    result = obj.addBinary(a,b)
    print(f"a={a},b={b}, result ={result}")

    a = "11"
    b = "11"
    result = obj.addBinary(a, b)
    print(f"a={a},b={b}, result ={result}")

    a = "1010"
    b = "1011"
    result = obj.addBinary(a, b)
    print(f"a={a},b={b}, result ={result}")




