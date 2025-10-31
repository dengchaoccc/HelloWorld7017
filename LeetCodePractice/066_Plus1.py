#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/30 15:02
# @Author  : mac
# @File    : 066_Plus1.py
# @Software: PyCharm
'''
066 加1
给定一个表示 大整数 的整数数组 digits，其中 digits[i] 是整数的第 i 位数字。
这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 0。
将大整数加 1，并返回结果的数字数组。
示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
加 1 后得到 123 + 1 = 124。
因此，结果应该是 [1,2,4]。
示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
加 1 后得到 4321 + 1 = 4322。
因此，结果应该是 [4,3,2,2]。
示例 3：
输入：digits = [9]
输出：[1,0]
解释：输入数组表示数字 9。
加 1 得到了 9 + 1 = 10。
因此，结果应该是 [1,0]。
'''

'''
python知识点：
1，如何把list 的元素翻转
2，如何做数字相加和进位
'''


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        result = []
        digits2 = [0] * len(digits)  # 把位数补齐,最后一个写1，其他全部写0
        digits2[-1] = 1
        extra_add = 0 #进位

        for i in range(len(digits) - 1, -1, -1):
            sum = digits[i] + digits2[i] + extra_add
            extra_add = int(sum / 10)
            result.append(sum % 10)
        if extra_add > 0:
            result.append(extra_add)
        result.reverse()
        return result

if __name__ == "__main__":
    obj = Solution()
    digits = [1, 2, 3]
    result = obj.plusOne(digits)
    print(f" digits={digits},result={result}")

    digits = [1, 2, 9]
    result = obj.plusOne(digits)
    print(f" digits={digits},result={result}")

    digits = [9]
    result = obj.plusOne(digits)
    print(f" digits={digits},result={result}")