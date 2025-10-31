#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/31 10:10
# @Author  : mac
# @File    : 202_HappyNumber.py
# @Software: PyCharm
'''
202: 快乐数
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」 定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
1 <= n <= 2 31 - 1

示例 1：
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
示例 2：

输入：n = 2
输出：false

思路有2个：
1，使用哈希，访问过的值就存起来，如果是死循环，必然会访问到之前保存的值
2，使用快慢指针，一个一次走一步，一个走两步。如果是死循环形成的环，她们必然会相遇
'''

'''
python  知识点：
1，没有do-while 的语法，使用while True 替代
2，使用快慢指针检查是否有环的存在
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        #根据算法要求，挨个数字拆开求平方，获取下一个数
        def get_next(i):
            sum = 0
            beichu = i
            while beichu > 0:
                yushu = beichu % 10
                sum += yushu ** 2
                beichu = int(beichu / 10)
            return sum

        # 一个指针一次走一步，一个指针一次走两步，要么最后为1，要么最后相遇
        fast = n
        slow = n

        while True:
            fast = get_next(get_next(fast))
            slow = get_next(slow)

            if fast == 1 or slow == 1:
                return True
            if fast == slow:
                return False
        return False

if __name__ == "__main__":
    obj = Solution()
    n = 19
    result = obj.isHappy(n)
    print(f"n={n},result={result}")

    n = 9
    result = obj.isHappy(n)
    print(f"n={n},result={result}")

    n = 2
    result = obj.isHappy(n)
    print(f"n={n},result={result}")

    n = 1
    result = obj.isHappy(n)
    print(f"n={n},result={result}")

    n = 1624
    result = obj.isHappy(n)
    print(f"n={n},result={result}")

