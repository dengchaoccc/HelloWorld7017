

'''
removeDuplicates
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

'''

'''
解题思路：
既然是有序的，那么我就在原来的数组上建立一个栈，然后新入站的元素，比size -2，就是顶部-2位置的元素一样，就不入栈
因为已经重复了超过2个了，否则就入栈。
这里为了训练一些函数常用的坑，我额外用一些空间
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前七个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
'''

"""
:type nums: List[int]
:rtype: int
"""
def removeDuplicates( nums):

    #如果只有2个元素，肯定不会重复，直接返回即可
    if (len(nums) <=2):
        return len(nums)

    # 只要新加入的元素和栈顶-2的元素不同就可以
    stack = []
    stack_size = 2
    stack.append(nums[0])
    stack.append(nums[1])

    for i in range(2, len(nums)):
        if (nums[i] != stack[-2]):
            stack.append(nums[i])
    '''
    这里有坑，需要注意:
    1, 如果使用了nums = list(stack)相当于创建了一个新对象，这个对象在栈内，函数关闭就消失了，会出问题
    2，如果使用了nums= stack[:]也不行，n创建新对象
    3，nums[:] = stack - 修改原对象内容
    '''
    nums[:] = stack

    return len(nums)

def test_repeat():
    #测试，每个元素最多留2个
    nums = [0,0,1,1,1,1,2,3,3,3,3]
    len1 = removeDuplicates(nums)
    print("after remove:len = {}, nums= {}", len1, nums)

test_repeat()