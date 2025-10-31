#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/29 16:58
# @Author  : mac
# @File    : 071_SimpfiledPath.py
# @Software: PyCharm
'''
071  简化路径
给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为 更加简洁的规范路径。
在 Unix 风格的文件系统中规则如下：
一个点 '.' 表示当前目录本身。
此外，两个点 '..' 表示将目录切换到上一级（指向父目录）。
任意多个连续的斜杠（即，'//' 或 '///'）都被视为单个斜杠 '/'。
任何其他格式的点（例如，'...' 或 '....'）均被视为有效的文件/目录名称。
返回的 简化路径 必须遵循下述格式：
始终以斜杠 '/' 开头。
两个目录名之间必须只有一个斜杠 '/' 。
最后一个目录名（如果存在）不能 以 '/' 结尾。
此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
返回简化后得到的 规范路径 。

示例 1：
输入：path = "/home/"
输出："/home"
解释：
应删除尾随斜杠。

示例 2：
输入：path = "/home//foo/"
输出："/home/foo"
解释：
多个连续的斜杠被单个斜杠替换。

示例 3：
输入：path = "/home/user/Documents/../Pictures"
输出："/home/user/Pictures"
解释：
两个点 ".." 表示上一级目录（父目录）。

示例 4：
输入：path = "/../"
输出："/"
解释：
不可能从根目录上升一级目录。

示例 5：
输入：path = "/.../a/../b/c/../d/./"
输出："/.../b/d"
解释：
"..." 在这个问题中是一个合法的目录名
'''

'''
python 知识点：
字符串的分割，拼凑
还有range 对象，其实就是切片
range(0,len(nums)  等效 nums[0:] 或者nums[:]
'''

class Solution:
    def simplifyPath(self, path: str) -> str:

        names = []
        stack: list[str] = []
        result_path: str = ""
        #根据斜杠，分割成多个字符，多个连续斜杠可能会分割出来空字符串
        names = path.split('/')
        path_num = len(names)

        for i in range(0, path_num):
            if names[i] == "." or names[i] == '/' or names[i] == "":
                continue
            #遇到..要出栈，上次保存的目录要删除，当然前提是上层非空
            if names[i] == "..":
                if len(stack) > 0:
                    stack.pop()
                continue
            #目录一个一个入栈，之后连接起来即可
            stack.append(names[i])


        for i in range(0, len(stack)):
            result_path += "/"
            result_path += stack[i]
        #特殊情况，空字符串也要加一个斜杠
        if result_path == "":
            result_path = "/"

        return result_path

if __name__ == "__main__":
    obj = Solution()
    path = "/home//foo/"
    result = obj.simplifyPath(path)
    print(f"patch = {path}, result = {result}")

    path = "/home/user/Documents/../Pictures"
    result = obj.simplifyPath(path)
    print(f"patch = {path}, result = {result}")

    path = "/../"
    result = obj.simplifyPath(path)
    print(f"patch = {path}, result = {result}")

    path = "/ ... / a /../ b / c /../ d /./"
    result = obj.simplifyPath(path)
    print(f"patch = {path}, result = {result}")

