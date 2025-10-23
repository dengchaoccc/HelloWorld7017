'''

Palindrome
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
示例 1：
输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
'''

'''
 知识点：
 1, 怎么做强制类型转换，并且从str类中获取对应的字符
 2, 怎么强制类型转换为int 或者其他类型
 :type x: int
:rtype: bool
 '''
def isPalindrome( x):
    if x < 0:
        return  False

    temp = str(x)
    temp_len = len(temp)
    for i in range(0, int(temp_len / 2) ):
        if temp[i] != temp[-1 - i]:
            return False
    return True
def test_palindrome():
    x = 1221
    result = isPalindrome(x)
    print(f"x = {x}, result = {result}")

test_palindrome()