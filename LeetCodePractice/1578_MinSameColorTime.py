#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/3 11:18
# @Author  : mac
# @File    : 1578_MinSameColorTime.py
# @Software: PyCharm
'''
1578:中级 使绳子变成彩色的最短时间
Alice 把 n 个气球排列在一根绳子上。给你一个下标从 0 开始的字符串 colors ，其中 colors[i] 是第 i 个气球的颜色。
Alice 想要把绳子装扮成 五颜六色的 ，且她不希望两个连续的气球涂着相同的颜色，
所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成 彩色 。给你一个 下标从 0 开始 的整数数组 neededTime ，
其中 neededTime[i] 是 Bob 从绳子上移除第 i 个气球需要的时间（以秒为单位）。
返回 Bob 使绳子变成 彩色 需要的 最少时间

输入：colors = "abaac", neededTime = [1,2,3,4,5]
输出：3
解释：'a' 是蓝色，'b' 是红色且 'c' 是绿色。
Bob 可以移除下标 2 的蓝色气球。这将花费 3 秒。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 3 。


输入：colors = "abc", neededTime = [1,2,3]
输出：0
解释：绳子已经是彩色的，Bob 不需要从绳子上移除任何气球。

输入：colors = "aabaa", neededTime = [1,2,3,4,1]
输出：2
解释：Bob 会移除下标 0 和下标 4 处的气球。这两个气球各需要 1 秒来移除。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 1 + 1 = 2 。
'''

#这个题目是利用贪心算法和反向思维，看起来是计算最少时间，实际上是保留最大时间
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        '''
        思路：如果有相邻的颜色，只保留删除成本最高颜色，其他的颜色全部删掉
        然后统计删掉需要的时间和成本
        '''
        color_len = len(colors)

        i = 0
        remove_total = 0

        while (i < color_len):
            one_color = colors[i]
            max_time = 0
            same_color_sum = 0
            #从这个位置往后看，如果颜色一样，只保留最大的，其他的计入删除
            while(i < color_len ) and (one_color == colors[i]):
                max_time = max(max_time, neededTime[i])
                same_color_sum += neededTime[i]
                i += 1
            #总时间，扣除保留的最大时间剩余的就是被删除的需要的时间
            remove_total = remove_total + same_color_sum - max_time
        return remove_total

if __name__ == "__main__":
    obj = Solution()
    colors = "abaac"
    neededTime = [1, 2, 3, 4, 5]
    result = obj.minCost(colors,neededTime)
    print(f"colors = {colors}, need time={neededTime},result = {result}")

    colors = "abc"
    neededTime = [1, 2, 3]
    result = obj.minCost(colors, neededTime)
    print(f"colors = {colors}, need time={neededTime},result = {result}")

    colors = "aabaa"
    neededTime = [1, 2, 3, 4, 1]
    result = obj.minCost(colors, neededTime)
    print(f"colors = {colors}, need time={neededTime},result = {result}")