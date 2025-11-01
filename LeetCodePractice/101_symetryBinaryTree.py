#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/31 19:38
# @Author  : mac
# @File    : 101_symetryBinaryTree.py
# @Software: PyCharm
'''
101:对称二叉树

给你一个二叉树的根节点 root ， 检查它是否轴对称
输入：root = [1,2,2,3,4,4,3]
输出：true
输入：root = [1,2,2,null,3,null,3]
输出：false
'''
'''
解题思路：
用左右两个指针，分别从左和从右边遍历二叉树，如果数值多一样则对称
'''

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check(self, p, q):
            if (not q) and (not p):
                return True
            if (not q) or (not p):
                return False
            if p.val != q.val:
                return False

            val1 = self.check(p.left, q.right)
            val2 = self.check(p.right, q.left)
            return val1 and val2

    '''
    Optional[TreeNode] 等价于 Union[TreeNode, None]，意思是：
    参数 root 可以是 TreeNode 类型
    或者可以是 None
    '''
    def isSymmetric(self, root:Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)


if __name__ == "__main__":
    obj = Solution()
    root = [1,2,2,3,4,4,3]
    result = obj.isSymmetric(root)
    print(f" tree={root},result={result}")

    root = [1,2,2,None,3,None,3]
    result = obj.isSymmetric(root)
    print(f" tree={root},result={result}")

