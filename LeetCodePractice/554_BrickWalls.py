#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/4 10:47
# @Author  : mac
# @File    : 554_BrickWalls.py
# @Software: PyCharm
'''
554 中级 砖墙
你的面前有一堵矩形的、由 n 行砖块组成的砖墙。这些砖块高度相同（也就是一个单位高）但是宽度不同。每一行砖块的宽度之和相等。
你现在要画一条 自顶向下 的、穿过 最少 砖块的垂线。如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。
你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。
给你一个二维数组 wall ，该数组包含这堵墙的相关信息。
其中，wall[i] 是一个代表从左至右每块砖的宽度的数组。
你需要找出怎样画才能使这条线 穿过的砖块数量最少 ，并且返回 穿过的砖块数量 。

输入：wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
输出：2
示例 2：

输入：wall = [[1],[1],[1]]
输出：3

提示：
n == wall.length
1 <= n <= 104
1 <= wall[i].length <= 104
1 <= sum(wall[i].length) <= 2 * 104
对于每一行 i ，sum(wall[i]) 是相同的
1 <= wall[i][j] <= 231 - 1
'''

'''
python 知识点：
1，字典如何统计出现次数
2，字典如何获取value值
3，字典函数get需要设置默认值
4，二维数组的遍历方法
'''
class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        # 二维数组，记录裂缝出现的位置
        gaps = []
        # 把墙砖转换为缝隙的位置
        for i in range(len(wall)):
            row = wall[i]
            row_gap = []
            position = 0

            for j in wall[i]:
                position += j
                row_gap.append(position)

            # 墙的最右边是不算有效的，所以删除这个边界
            row_gap.pop()
            gaps.append(row_gap)

        # 开始统计每种裂缝出现的次数，裂缝最多的地方就是穿越次数最少得
        gap_count = {}
        max_gap = 0
        for i in range(0, len(gaps)):
            for j in gaps[i]:
                gap_count[j] = gap_count.get(j, 0) + 1
                max_gap = max(max_gap, gap_count[j])

        return len(wall) - max_gap


if __name__ == "__main__":
    obj = Solution()
    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    result = obj.leastBricks(wall)
    print(f"wall = {wall}, result = {result}")

    wall = [[1, 2], [1, 1, 1], [1, 2], [3], [1, 2], [2, 1]]
    result = obj.leastBricks(wall)
    print(f"wall = {wall}, result = {result}")

    wall = [[1], [1], [1]]
    result = obj.leastBricks(wall)
    print(f"wall = {wall}, result = {result}")

