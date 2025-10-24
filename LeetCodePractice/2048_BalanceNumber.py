#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/10/24 13:04
# @Author  : mac
# @File    : 2048_BalanceNumber.py
# @Software: PyCharm
'''
2048:下一个更大的平衡数 中级
如果整数  x 满足：对于每个数位 d ，这个数位 恰好 在 x 中出现 d 次。那么整数 x 就是一个 数值平衡数 。
给你一个整数 n ，请你返回 严格大于 n 的 最小数值平衡数 。
示例 1：
输入：n = 1
输出：22
解释：
22 是一个数值平衡数，因为：
- 数字 2 出现 2 次
这也是严格大于 1 的最小数值平衡数。

示例 2：
输入：n = 1000
输出：1333
解释：
1333 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。
这也是严格大于 1000 的最小数值平衡数。
'''

'''
python知识点：
1，如何初始化一个一维数组
2，pyton里没有标注变量类型，就有变成小数的情况，要int（）强制转化一下
3，Python 没有do-while的写法，只能用while True ,然后加一个break
'''
def is_Balance( num):
    beichushu = num

    # 一共就是0到9的数字
    digit_count = [0] * 10
    # 加个标志位,表示数字是否存在
    digit_valid = [0] * 10

    # python里没有do-while的写法，用这种方式来实现
    while True:
        chushu = int(beichushu / 10)
        yushu = int(beichushu % 10)
        digit_count[yushu] += 1
        digit_valid[yushu] = 1
        beichushu = chushu
        if beichushu <= 0:
            break

    for i in range(0, 10):
        if i != digit_count[i] and digit_valid[i]:
            return False

    return True


def nextBeautifulNumber( n: int) -> int:
    for i in range(n + 1, 100000000):
        if is_Balance(i):
            return i

def test_next_balance():
    num = 1
    balance = nextBeautifulNumber(num)
    print(f"num={num}, balance ={balance}")

    num = 1000
    balance = nextBeautifulNumber(num)
    print(f"num={num}, balance ={balance}")

    num = 3000
    balance = nextBeautifulNumber(num)
    print(f"num={num}, balance ={balance}")

    num = 1000000
    balance = nextBeautifulNumber(num)
    print(f"num={num}, balance ={balance}")
test_next_balance()