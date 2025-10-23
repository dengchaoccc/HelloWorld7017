'''
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
'''

"""
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
"""

def merge( nums1:int, m:int, nums2:int, n:int):

    tempNums:list[int] = []

    for i in range(0, m ):
        tempNums.append(nums1[i])
    for i in range(0, n):
        tempNums.append(nums2[i])
    tempNums.sort()
    nums1.clear()

    #new_list = old_list.copy()也可以的  new_list = old_list[:]
    for i in range(0, m + n):
        nums1.append(tempNums[i])

    return nums1

def test_merge():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)

    print(nums1)

test_merge()