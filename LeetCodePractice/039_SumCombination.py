#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/5 16:19
# @Author  : mac
# @File    : 039_SumCombination.py
# @Software: PyCharm

'''
39,中等，组合总和
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为 target 的不同组合数少于 150 个。


示例 1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

示例 2：
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：
输入: candidates = [2], target = 1
输出: []


提示：
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40
'''

class Solution:
    '''
    递归遍历，这个函数的特殊点，就在于start下标，可以防止重复子集的生成
    '''
    def dfs(self, nums, target, start, current, answer):
        #1, 设置终止条件，找到就返回，题目保证150次必定有结果
        if target == 0:
            #这里有坑，千万不要answer.append(current)，这存的是对象而不是副本
            one_combination = list(current)
            answer.append(one_combination)
            return
        #2, 开始遍历其他可能性
        for i in range(start, len(nums)):
            #3，做剪枝处理
            if nums[i] > target:
                return
            #4, 开始入栈
            current.append(nums[i])
            #这里把start 变成i ，就不会出现用了[1,4,5] 还出现[1,5,4]的情况
            self.dfs(nums,target-nums[i], i,current,answer)
            #6,当前节点出栈
            current.pop()


    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        nums = sorted(candidates)
        current = []#当前的序列，存在这里
        answer = [] #用来保存结果

        self.dfs(nums,target,0, current,answer)

        return answer


if __name__ == "__main__":
    obj = Solution()
    candidates = [1,2,3,4]
    target = 6
    result = obj.combinationSum(candidates, target)
    print(f"candidates = {candidates}, target={target} result = {result}")

    candidates = [2, 3, 6,7]
    target = 7
    result = obj.combinationSum(candidates, target)
    print(f"candidates = {candidates}, target={target} result = {result}")

    candidates = [2, 3, 5]
    target = 8
    result = obj.combinationSum(candidates, target)
    print(f"candidates = {candidates}, target={target} result = {result}")




