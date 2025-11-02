#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/2 15:05
# @Author  : mac
# @File    : 3217_RemoveLinklistNode.py
# @Software: PyCharm
'''
3217: 从链表中删除数组中存在的节点
给你一个整数数组 nums 和一个链表的头节点 head。从链表中移除所有存在于 nums 中的节点后，返回修改后的链表的头节点。



示例 1：
输入： nums = [1,2,3], head = [1,2,3,4,5]
输出： [4,5]

输入： nums = [1], head = [1,2,1,2,1,2]
输出： [2,2,2]
'''

'''
python知识：
1，pycharm中，command + / 可以批量注释代码
2，Optional[Type] 等价于 Union[Type, None]，意思是"这个变量可以是 Type 类型，或者是 None"。
3, 函数传值和改变引用，要特别注意赋值的时候会有问题：
 def remove_one_node(self, node, head):
    if head == node:
        head = head.next  # 这里只是改变了函数内部的 head 引用
        return
# 调用后，外部的 head 还是指向原来的节点

使用返回值或者类传入都可以
def remove_one_node(self, node):
        # 删除头节点
        if self.head == node:
            self.head = self.head.next
            return
            
4，循环使用while和使用for变量出来的结果是不同的。
   情景一：
        temp = head
        while temp:
            temp = next_node
        这里循环跳出以后，temp是空
   情景二：
        for temp in nums:
            arry.append(temp)
        这里temp是数组中最后一个值。C语言和Java，for循环出来以后，这个值是空的
'''

from typing import  Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    '''
    head = head.next  # 这里只是改变了函数内部的 head 引用，是不行的
    '''

    def remove_one_node(self, node, head):
        # 删除的是头节点，要特殊处理
        if head == node:
            return head.next

        prev = head
        temp = prev.next
        while temp:
            if temp == node:
                prev.next = node.next
                return head
            else:
                prev = temp
                temp = temp.next
        return head

    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head
        while temp:
            next_node = temp.next

            if temp.val in nums:
                #print(f"before move {temp.val} head = {head}")
                head = self.remove_one_node(temp, head)
                #print(f"after move head={head}")
            temp = next_node
        return head



if __name__ == "__main__":

    def construct_list(nums):
        head = None
        for i in nums:
            temp_node = ListNode(i,None)
            if not head:
                head = temp_node
            else:
                loop = head
                while loop:
                    if not loop.next:
                        loop.next = temp_node
                        break
                    loop = loop.next
        return head

    obj = Solution()
    origin_nums = [1, 2, 3, 4, 5]
    num_to_del =[1,3]
    list_head = construct_list(origin_nums)
    result = obj.modifiedList(num_to_del, list_head)
    print(f"nums = {origin_nums},nums to del {num_to_del} result = {result.val}")