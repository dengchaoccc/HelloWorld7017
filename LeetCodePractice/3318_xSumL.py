#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/4 18:04
# @Author  : mac
# @File    : 3318_xSumL.py
# @Software: PyCharm
'''
给你一个由 n 个整数组成的数组 nums，以及两个整数 k 和 x。
数组的 x-sum 计算按照以下步骤进行：
统计数组中所有元素的出现次数。
仅保留出现次数最多的前 x 个元素的每次出现。如果两个元素的出现次数相同，则数值 较大 的元素被认为出现次数更多。
计算结果数组的和。
注意，如果数组中的不同元素少于 x 个，则其 x-sum 是数组的元素总和。
返回一个长度为 n - k + 1 的整数数组 answer，其中 answer[i] 是 子数组 nums[i..i + k - 1] 的 x-sum。
子数组 是数组内的一个连续 非空 的元素序列。

示例 1：
输入：nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
输出：[6,10,12]
解释：
对于子数组 [1, 1, 2, 2, 3, 4]，只保留元素 1 和 2。因此，answer[0] = 1 + 1 + 2 + 2。
对于子数组 [1, 2, 2, 3, 4, 2]，只保留元素 2 和 4。因此，answer[1] = 2 + 2 + 2 + 4。注意 4 被保留是因为其数值大于出现其他出现次数相同的元素（3 和 1）。
对于子数组 [2, 2, 3, 4, 2, 3]，只保留元素 2 和 3。因此，answer[2] = 2 + 2 + 2 + 3 + 3。
示例 2：
输入：nums = [3,8,7,8,7,5], k = 2, x = 2
输出：[11,15,15,15,12]
解释：
由于 k == x，answer[i] 等于子数组 nums[i..i + k - 1] 的总和。
提示：
1 <= n == nums.length <= 50
1 <= nums[i] <= 50
1 <= x <= k <= nums.length
'''
'''
解题思路： 就是要明白这个题目想干嘛，它就是想计算长度为k的子数组，统计出现次数，然后对出现次数最多的求和
python知识点：
1，如何做排序
2，使用sorted之后，返回的是一个list，而不是dict类型了
3，对于滑动窗口的问题，每次更新都维护好窗口
4，排序，如果有两个要考虑的维度，a要升序，b要降序，该怎么排序
'''


class Solution:
    # 从当前的字典里，按照题目的要求，获取sum x
    def get_x_sum(self, sub_nums_count, x):
        # 先排序,按照value 降序，再按照key降序
        sorted_nums = sorted(sub_nums_count.items(), key=lambda x: (-x[1], -x[0]))
        len1 = len(sorted_nums)
        end = min(len1, x)

        top_x_sum = 0
        #统计出现次数最多的元素，求和
        for i in range(0, end):
            top_x_sum += sorted_nums[i][0] * sorted_nums[i][1]

        return top_x_sum

    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        # 找出所有长度为k的子数组，并且记录x-sum，要注意边界值
        # x-sum 就是长度为k的子数组里，出现次数TOPx的数字的和，次数一样就取数字大的
        n = len(nums)

        # 用来存储子数组的数字出现次数
        sub_nums_count = {}
        answer = []
        # 子数组的个数为为 n - k + 1
        for i in range(0, n - k + 1):
            # 第一次计算，把统计窗口初始化
            if i == 0:
                for j in range(i, i + k - 1):
                    sub_nums_count[nums[j]] = sub_nums_count.get(nums[j], 0) + 1
            # 每次窗口有移动，把最后一个元素加进去
            in_value = nums[i + k - 1]
            sub_nums_count[in_value] = sub_nums_count.get(in_value, 0) + 1

            # 计算窗口里的x-sum
            temp_x_sum = self.get_x_sum(sub_nums_count, x)
            answer.append(temp_x_sum)

            # 窗口右移了，最左边的元素吐出来
            sub_nums_count[nums[i]] = sub_nums_count.get(nums[i], 0) - 1

        return answer


if __name__ == "__main__":
    obj = Solution()
    nums = [1,1,2,2,3,4,2,3]
    k = 6
    x = 2
    result = obj.findXSum(nums,k, x)
    print(f"nums = {nums}, k={k},x ={x}, result = {result}")

    nums = [3,8,7,8,7,5]
    k = 2
    x = 2
    result = obj.findXSum(nums, k, x)
    print(f"nums = {nums}, k={k},x ={x}, result = {result}")