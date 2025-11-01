#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/1 13:14
# @Author  : mac
# @File    : 046_FullCombination.py
# @Software: PyCharm
'''
046， 全排列 中级
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
nums 中的所有整数 互不相同
示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：
输入：nums = [1]
输出：[[1]]
'''
'''
python 知识：
1， 如果做深度优先递归调用
2， 如何使用切片做副本拷贝
3， 注意列表的append 添加的是对象，而不是值。 如果要值，就要append 对象的切片，非常重要
'''
class Solution:
    def dfs(self, nums,  current, result):
        #1 定义递归的终止条件
        if len(current) == len(nums):
            #print(f"append{current}")
            #这一行非常关键，不能append(current)，这样你只是存了对象，没有存副本
            #一定要存切片
            result.append(current[:])
            return
        #2 当前节点入栈
        for x in nums:
            #用过的节点不再使用
            if x in current:
                continue
            #3 当前数字入栈
            current.append(x)
            #4 递归到下一层,找下一个数字
            self.dfs(nums, current, result)
            #5 递归完了之后出栈
            current.pop()
        return


    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current =[]
        self.dfs(nums,current,result)
        #print(f"reuslt = {result}")
        return result

if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3]
    result = obj.permute(nums)
    print(f"nums = {nums}, result = {result}")

    nums = [1]
    result = obj.permute(nums)
    print(f"nums = {nums}, result = {result}")

    nums = [1,3,4,5]
    result = obj.permute(nums)
    print(f"nums = {nums}, result = {result}")

    nums = [0]
    result = obj.permute(nums)
    print(f"nums = {nums}, result = {result}")

