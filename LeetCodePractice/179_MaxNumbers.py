#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/2 16:48
# @Author  : mac
# @File    : 179_MaxNumbers.py
# @Software: PyCharm
'''
179,组成的最大数 中级
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
示例 1：
输入：nums = [10,2]
输出："210"
示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"

'''

'''
python知识点：
1，排序如何定义哪个数字排在前面
2，如何指定自己的排序函数
3，cmp_to_key的导入
'''
from functools import cmp_to_key
class Solution:
    '''
    这个就是算法的核心，自定义排序函数
    首先看最左边谁更大，接着第二左边……，转换为str类型可以直接比对
    Python 的字符串比较中，
    对于 [4,42]，比较 442>424，需要把 4 放在前面；
    对于 [4,45]，比较 445<454，需要把 45 放在前面。
    '''

    def largestNumber(self, nums: list[int]) -> str:
        def compare(a, b):
            temp_a = str(a)
            temp_b = str(b)
            # 返回负数表示 a 应该排在 b 前面
            # 返回正数表示 a 应该排在 b 后面
            # 返回 0 表示相等
            if (temp_a + temp_b) > (temp_b + temp_a):
                return -1
            elif (temp_a + temp_b) < (temp_b + temp_a):
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(compare))

        anwser = ""
        # 0开头的情况，把0的前缀去掉
        if 0 == nums[0]:
            return "0"

        for i in nums:
            anwser = anwser + str(i)
        return anwser


if __name__ == "__main__":
    obj = Solution()
    nums = [10,2]
    result = obj.largestNumber(nums)
    print(f"nums={nums},result ={result}")

    nums = [3,30,34,5,9]
    result = obj.largestNumber(nums)
    print(f"nums={nums},result ={result}")

    nums = [4, 45, 42, 43]
    result = obj.largestNumber(nums)
    print(f"nums={nums},result ={result}")
