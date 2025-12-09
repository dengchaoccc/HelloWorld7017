#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/22 12:22
# @Author  : mac
# @File    : 14_Iter.py
# @Software: PyCharm
'''
迭代器的测试，很简单
迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。

生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。
然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，
直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。
'''

def iter_test():
    array = [1,34,2,445,56,6676,4]
    it = iter(array)
    #执行以后，下一句就一定到index 1 了，迭代器不能返回置零
    print(next(it))

    for x in it:
        print(x)



def countdown(n):
    while n > 0:
        yield n
        n -= 1

def test_generator():
    gen = countdown(5)
    print(next(gen))
    print(next(gen))
    print(next(gen))


if __name__ == "__main__":
    iter_test()
    test_generator()

