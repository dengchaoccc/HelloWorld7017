#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/23 21:14
# @Author  : mac
# @File    : 012_NumberToRoman.py
# @Software: PyCharm
'''
七个不同的符号代表罗马数字，其值如下：
符号	值
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：
如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。
如果该值以 4 或 9 开头，使用 减法形式，表示从以下符号中减去一个符号，
例如 4 是 5 (V) 减 1 (I): IV ，9 是 10 (X) 减 1 (I)：IX。
仅使用以下减法形式：4 (IV)，9 (IX)，40 (XL)，90 (XC)，400 (CD) 和 900 (CM)。
只有 10 的次方（I, X, C, M）最多可以连续附加 3 次以代表 10 的倍数。
你不能多次附加 5 (V)，50 (L) 或 500 (D)。如果需要将符号附加4次，请使用 减法形式。
给定一个整数，将其转换为罗马数字。


示例 1：
输入：num = 3749
输出： "MMMDCCXLIX"
解释：
3000 = MMM 由于 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC 由于 500 (D) + 100 (C) + 100 (C)
  40 = XL 由于 50 (L) 减 10 (X)
   9 = IX 由于 10 (X) 减 1 (I)
注意：49 不是 50 (L) 减 1 (I) 因为转换是基于小数位
'''
'''
解题思路：贪心算法
4，,9，,40，,90这些特殊数字也有表示方式，需要放进来
使用找零钱一样的贪心算法，尽量找面额大的去填充，转换成字符串
比如3749， 先找到1000M， 每找到一次余数-1000，最后凑了3个M后余数变成749
接着找D 500，之后余数变成249
接着找C 100 ，找了两次以后就剩下49
40这里是没有原始的表示的，这里要额外给一个XL表示40
最后9也是没有原始表示，用IX表示
'''

'''
python知识点：
1，字符串如何拼接
2，字典的成员如何构造，如何遍历
'''
def intToRoman( num: int) -> str:
    # 这个查表，把40,90,400,900都放进去了
    num_to_roman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    result_str = ""
    rest_num = num

    # 一层一层的拼凑，从最大的1000开始找，题目规定最大值没超过4000
    for key, value in num_to_roman.items():
        while rest_num >= key:
            result_str += value  # 这样就把罗马数字字符串加到后头了
            rest_num -= key

    return result_str

def test_num_to_roman():
    num = 3749
    result = intToRoman(num)
    print(f"num={num},roman={result}")

    num = 4
    result =  intToRoman(num)
    print(f"num={num},roman={result}")

    num = 8
    result =  intToRoman(num)
    print(f"num={num},roman={result}")

    num = 1111
    result =  intToRoman(num)
    print(f"num={num},roman={result}")

test_num_to_roman()